#!/usr/bin/env python3
"""verify-repl-outputs.py — re-run REPL blocks through the Jayret CLI.

For each :::{.pyret-repl} div with a ```pyret block, run the (already-
translated) Jayret code through the CLI and replace the paired ```output
block with the actual output.  If invocation fails, leave the original
output block and insert a HTML comment marking the failure.

Caveat: the script will rewrite ANY block tagged ```jayret, even ones
that are demonstrating another language's REPL (e.g. a `python` block
that was mistakenly tagged `jayret` in the source).  Review the diff
before committing.  See intro-python.md §"Python console" for the kind
of section that needs `python` lang tags instead of `jayret`.

Usage:
  python3 tools/verify-repl-outputs.py --all [--dry-run] [--in-place]
  python3 tools/verify-repl-outputs.py --file <path.md> [--dry-run] [--in-place]

Requirements:
  - node and the jayret CLI at JAYRET_JS (see constant below)
  - libuuid.so.1 via LD_PRELOAD (NixOS; see LIBUUID_PATH)
  - Jayret server auto-starts on first invocation (~3-5s warm-up)
"""

import re
import sys
import os
import subprocess
import tempfile
import argparse
import glob
import time

JAYRET_JS = os.environ.get(
    'JAYRET_JS',
    '/home/artem/Dev/pyret/jayret-npm/jayret.js')

# NixOS: libuuid.so.1 isn't in the standard dynamic linker path.
LIBUUID_PATH = os.environ.get(
    'LD_PRELOAD',
    '/nix/store/gf6i4cbisapj28y2dnqhpk1s95vd2r36-util-linux-2.42-lib/lib/libuuid.so.1')

TIMEOUT = 30  # seconds per invocation

_server_started = False


def run_jayret(src_code: str) -> tuple[bool, str]:
    """Run src_code through the Jayret CLI, return (ok, output).

    Wraps the code so that the last expression's value is printed.
    If the code contains a newline it's treated as a multi-statement block;
    each statement is run as-is (they must be valid top-level Jayret).
    The last expression is wrapped in print(to-repr(EXPR) + "\n").

    Limitations:
    - Multi-line REPL sessions that depend on earlier bindings are run as
      a single file (sequentially), so they work if the code is self-contained.
    - Code that defines functions/data but has no expression to display is
      run as-is (no output expected).
    """
    global _server_started

    lines = src_code.strip().splitlines()

    def strip_semi(s: str) -> str:
        # Strip trailing `;` (Jayret statement terminator) so the expression
        # can be wrapped in to-repr(...) without a parse error.
        return s.rstrip().rstrip(';').rstrip()

    # Build a small Jayret program that prints the result of the final
    # expression (if there is one).  Everything before the last line is
    # emitted verbatim; the last line is wrapped.
    if len(lines) == 1:
        body = f'print(to-repr({strip_semi(lines[0])}) + "\\n")\n'
    else:
        # Check if the last line looks like an expression (not a decl/stmt
        # ending in a block) — heuristic: doesn't start with a keyword that
        # introduces a binding.
        last = lines[-1].strip()
        decl_keywords = ('void ', 'Object ', 'int ', 'boolean ', 'String ',
                         'data ', 'import ', 'provide', 'use ', '@Check', '@check',
                         '// ', '#')
        is_decl = any(last.startswith(k) for k in decl_keywords) or last == ''
        if is_decl:
            body = '\n'.join(lines) + '\n'
        else:
            body = '\n'.join(lines[:-1]) + '\n'
            body += f'print(to-repr({strip_semi(last)}) + "\\n")\n'

    with tempfile.NamedTemporaryFile(suffix='.jrt', mode='w',
                                     delete=False, encoding='utf-8') as f:
        f.write(body)
        tmp = f.name

    env = dict(os.environ)
    env['LD_PRELOAD'] = LIBUUID_PATH

    try:
        result = subprocess.run(
            ['node', JAYRET_JS, '-q', tmp],
            capture_output=True, text=True, timeout=TIMEOUT, env=env)
    except subprocess.TimeoutExpired:
        os.unlink(tmp)
        return False, 'timeout'
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass

    if result.returncode != 0:
        err = (result.stderr or result.stdout or '').strip()
        # Strip tmp-file paths and column markers (noise in TODO comments).
        err = re.sub(r'\s*at java-file:///tmp/[^\s]+\s*', ' ', err)
        # Collapse internal whitespace, take a one-line summary.
        err = re.sub(r'\s+', ' ', err).strip()
        return False, f'exit {result.returncode}: {err[:160]}'

    # Strip the "The program didn't define any tests." trailer that appears on
    # the same line as output when no newline follows print().
    raw = result.stdout
    raw = raw.replace("The program didn't define any tests.", '')
    # Also strip test-runner summary lines that appear at the end
    raw = re.sub(r'\n?(?:\d+/\d+ tests? passed.*|Looks shipshape.*)\s*$', '', raw)
    return True, raw.strip()


def warm_up():
    """Prime the compile server (takes ~3-5s on first call)."""
    global _server_started
    if _server_started:
        return
    print('Warming up Jayret compile server...', file=sys.stderr)
    ok, out = run_jayret('1')
    if not ok:
        print(f'Warning: warm-up failed: {out}', file=sys.stderr)
    else:
        print(f'Server ready.', file=sys.stderr)
    _server_started = True


def process_file(path: str, dry_run: bool, in_place: bool) -> dict:
    with open(path, encoding='utf-8') as f:
        src = f.read()

    lines = src.split('\n')
    out = []
    stats = {'total': 0, 'ok': 0, 'failed': 0, 'skipped': 0}

    i = 0
    while i < len(lines):
        line = lines[i]

        # Look for REPL div opener
        if re.match(r':::\s*\{\.pyret-repl\}', line):
            div_open = line
            out.append(line)
            i += 1

            # Collect everything until :::
            div_lines = []
            while i < len(lines) and not re.match(r'^:::\s*$', lines[i]):
                div_lines.append(lines[i])
                i += 1
            div_close = lines[i] if i < len(lines) else ':::'
            i += 1

            # Parse div contents: look for ```pyret block and ```output block
            j = 0
            pyret_block = None
            pyret_start = None
            output_block = None
            output_start = None
            output_end = None

            while j < len(div_lines):
                dl = div_lines[j]
                m = re.match(r'^(```+) ?(pyret|output|jayret)(.*)$', dl)
                if m:
                    ticks, lang, rest = m.groups()
                    # find closing fence
                    close_pat = ticks
                    body_lines = []
                    j += 1
                    while j < len(div_lines) and not div_lines[j].startswith(close_pat):
                        body_lines.append(div_lines[j])
                        j += 1
                    close_line = div_lines[j] if j < len(div_lines) else ticks
                    j += 1

                    if lang in ('pyret', 'jayret'):
                        pyret_block = '\n'.join(body_lines)
                        pyret_start = (len(out) + 1 + div_lines.index(dl)
                                       if dl in div_lines else None)
                    elif lang == 'output':
                        output_block = '\n'.join(body_lines)
                        output_start = dl
                        output_end = close_line
                else:
                    j += 1

            # Reconstruct div with possibly-replaced output block
            if pyret_block is not None and output_block is not None:
                stats['total'] += 1
                ok, actual = run_jayret(pyret_block)
                if ok:
                    stats['ok'] += 1
                    if actual != output_block.strip():
                        # Rebuild div_lines replacing output block content
                        new_div = _replace_output_in_div(
                            div_lines, output_block, actual)
                        out.extend(new_div)
                    else:
                        out.extend(div_lines)
                else:
                    stats['failed'] += 1
                    # Mark with TODO comment, leave original
                    new_div = list(div_lines)
                    new_div.insert(0, f'<!-- TODO(verify-repl): jayret failed: {actual} -->')
                    out.extend(new_div)
            elif pyret_block is not None:
                # Input-only div (no output block yet)
                stats['skipped'] += 1
                out.extend(div_lines)
            else:
                out.extend(div_lines)

            out.append(div_close)
            continue

        out.append(line)
        i += 1

    result = '\n'.join(out)
    changed = result != src

    if changed and in_place:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(result)

    return stats


def _replace_output_in_div(div_lines: list, old_output: str, new_output: str) -> list:
    """Replace the content of the ```output block in div_lines."""
    out = []
    j = 0
    while j < len(div_lines):
        dl = div_lines[j]
        m = re.match(r'^(```+) ?output(.*)$', dl)
        if m:
            ticks = m.group(1)
            out.append(dl)
            j += 1
            # skip old output body
            while j < len(div_lines) and not div_lines[j].startswith(ticks):
                j += 1
            # emit new output body
            for l in new_output.split('\n'):
                out.append(l)
            # emit close fence
            if j < len(div_lines):
                out.append(div_lines[j])
                j += 1
        else:
            out.append(dl)
            j += 1
    return out


def main():
    parser = argparse.ArgumentParser(description='Verify REPL outputs via Jayret CLI')
    parser.add_argument('--all', action='store_true', help='Process all src/*.md files')
    parser.add_argument('--file', help='Process a single file')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--in-place', action='store_true')
    ns = parser.parse_args()

    if ns.all:
        files = sorted(glob.glob('src/*.md'))
    elif ns.file:
        files = [ns.file]
    else:
        parser.print_help()
        sys.exit(1)

    warm_up()

    total = {'total': 0, 'ok': 0, 'failed': 0, 'skipped': 0}
    for f in files:
        stats = process_file(f, ns.dry_run, ns.in_place)
        if stats['total'] > 0 or stats['skipped'] > 0:
            print(f"{f}: {stats['ok']}/{stats['total']} ok, "
                  f"{stats['failed']} failed, {stats['skipped']} skipped")
        for k in total:
            total[k] += stats[k]

    print(f"\nTotal: {total['ok']}/{total['total']} ok, "
          f"{total['failed']} failed, {total['skipped']} input-only")


if __name__ == '__main__':
    main()
