#!/usr/bin/env python3
"""prose-rebrand-md.py — Pyret→Jayret in DCIC Markdown prose.

Applies URL and name substitutions outside fenced code blocks and
inline code spans.  Imports URL_SUBS / PROSE_SUBS from the sibling
jayret-docs prose-rebrand.py so fixes land in one place.

Usage:
  python3 tools/prose-rebrand-md.py [--dry-run] [--in-place] <file.md> [...]

Substitutions (same as jayret-docs):
  code.pyret.org      → jayret-lang.github.io/code
  (www.)?pyret.org    → jayret-lang.github.io
  Pyret (word)        → Jayret
  pyret (word)        → jayret
  .arr (extension)    → .jrt
"""

import re
import sys
import os
import argparse

JAYRET_DOCS_TOOLS = os.environ.get(
    'JAYRET_DOCS_TOOLS_PATH',
    os.path.join(os.path.dirname(__file__), '../../jayret-docs/tools'))


def _load_subs():
    """Import URL_SUBS / PROSE_SUBS from prose-rebrand.py via importlib
    (the hyphen in the filename prevents normal import syntax)."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'prose_rebrand',
            os.path.join(JAYRET_DOCS_TOOLS, 'prose-rebrand.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.URL_SUBS, mod.PROSE_SUBS
    except Exception as e:
        print(f"Warning: could not import prose-rebrand.py ({e}); using built-in patterns.",
              file=sys.stderr)
        return _builtin_subs()


def _builtin_subs():
    URL_SUBS = [
        (re.compile(r'\bcode\.pyret\.org'), 'jayret-lang.github.io/code'),
        (re.compile(r'\bcode\.jayret\.org'), 'jayret-lang.github.io/code'),
        (re.compile(r'\bwww\.pyret\.org'), 'jayret-lang.github.io'),
        (re.compile(r'(?<!code\.)(?<!www\.)\bpyret\.org\b'), 'jayret-lang.github.io'),
    ]
    PROSE_SUBS = URL_SUBS + [
        (re.compile(r'(?<![A-Za-z0-9_-])Pyret(?![A-Za-z0-9_-])'), 'Jayret'),
        (re.compile(r'(?<![A-Za-z0-9_@-])pyret(?![A-Za-z0-9_-])'), 'jayret'),
        (re.compile(r'\.arr(?![A-Za-z0-9_])'), '.jrt'),
    ]
    return URL_SUBS, PROSE_SUBS


URL_SUBS, PROSE_SUBS = _load_subs()


def apply_subs(text, subs):
    for pat, repl in subs:
        text = pat.sub(repl, text)
    return text


def _apply_inline(line, subs):
    """Apply subs to `line`, skipping backtick-delimited inline code spans."""
    out = []
    i = 0
    while i < len(line):
        if line[i] == '`':
            # find matching closing backtick (same run length)
            j = i + 1
            while j < len(line) and line[j] == '`':
                j += 1
            ticks = line[i:j]
            # find closing ticks
            end = line.find(ticks, j)
            if end == -1:
                # no close — treat rest as prose
                out.append(apply_subs(line[i:], subs))
                i = len(line)
            else:
                end_close = end + len(ticks)
                # skip optional {.attr} after closing ticks
                attr_m = re.match(r'\{[^}]*\}', line[end_close:])
                attr_end = end_close + (len(attr_m.group(0)) if attr_m else 0)
                out.append(line[i:attr_end])  # preserve code span + attr verbatim
                i = attr_end
        else:
            # find next backtick
            nxt = line.find('`', i)
            if nxt == -1:
                out.append(apply_subs(line[i:], subs))
                i = len(line)
            else:
                out.append(apply_subs(line[i:nxt], subs))
                i = nxt
    return ''.join(out)


def translate_markdown(src):
    lines = src.split('\n')
    out = []
    stats = {'changed': 0, 'lines': len(lines)}
    i = 0
    inside_fence = False
    fence_ticks = ''
    fence_indent = ''

    while i < len(lines):
        line = lines[i]

        if inside_fence:
            # Look for matching close fence
            if line.startswith(fence_indent + fence_ticks):
                inside_fence = False
            # Inside a code fence — apply URL_SUBS only (safe in any context)
            new_line = apply_subs(line, URL_SUBS)
        else:
            # Check for fence opener — track ALL fence languages so the
            # closing ``` is always matched.  Prose subs are skipped inside
            # any fenced block; URL_SUBS are applied inside (safe everywhere).
            m = re.match(r'^(\s*)(```+|~~~+) ?(\S*)(.*)$', line)
            if m:
                indent, ticks, lang, rest = m.groups()
                inside_fence = True
                fence_ticks = ticks
                fence_indent = indent
                # Inside code fences → URL_SUBS only
                new_line = apply_subs(line, URL_SUBS)
            else:
                # Regular prose line — apply full PROSE_SUBS but skip inline code
                new_line = _apply_inline(line, PROSE_SUBS)

        if new_line != line:
            stats['changed'] += 1
        out.append(new_line)
        i += 1

    return '\n'.join(out), stats


def main():
    parser = argparse.ArgumentParser(description='Prose rebrand for DCIC Markdown')
    parser.add_argument('files', nargs='+')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--in-place', action='store_true')
    ns = parser.parse_args()

    total_changed = 0
    for f in ns.files:
        with open(f, encoding='utf-8') as fh:
            src = fh.read()
        out, stats = translate_markdown(src)
        changed = out != src
        total_changed += stats['changed']
        if stats['changed'] or ns.dry_run:
            print(f"{f}: {stats['changed']} lines changed")
        if ns.in_place and changed:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(out)

    print(f"\nTotal lines changed: {total_changed}")


if __name__ == '__main__':
    main()
