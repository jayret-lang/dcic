#!/usr/bin/env python3
"""
add-scribble-anchors.py — one-shot tool to add Scribble-form name anchors.

Every source heading that carries an explicit `{#slug}` attribute generates
a heading id="slug" in the HTML.  The in-page mini-TOC tables (preserved as
raw HTML in the markdown) link to `#%28part._slug%29` — i.e. URL-encoded
`(part._slug)`.  Because the headings only have the plain slug id, those
TOC links resolve nowhere.

This script inserts a tiny raw-HTML block directly above each such heading:

    ```{=html}
    <a name="(part._slug)"></a>
    ```

Pandoc passes it through verbatim, so the resulting HTML has both:
    <h4 id="slug"><span ...>...</span></h4>
preceded by:
    <a name="(part._slug)"></a>

Both fragment forms (`#slug` and `#%28part._slug%29`) then work.

Idempotent: headings that already have the anchor block above them are
left unchanged.

Usage:
    python3 tools/add-scribble-anchors.py src/*.md
    python3 tools/add-scribble-anchors.py src/getting-started.md
"""

import re
import sys

# Matches an ATX heading with an explicit {#slug} attribute.
# group(1) = hashes, group(2) = rest of heading text (including {#slug})
# group(3) = the slug itself
HEADING_RE = re.compile(r'^(#{1,6})\s+(.+?)\s+\{#([^}]+)\}\s*$')

# What a Scribble anchor raw-HTML block looks like for a given slug.
def anchor_block(slug: str) -> str:
    return (
        '```{=html}\n'
        f'<a name="(part._{slug})"></a>\n'
        '```\n'
    )


def anchor_already_present(lines: list, heading_idx: int, slug: str) -> bool:
    """True if the heading at `heading_idx` is already preceded by our anchor."""
    target = f'<a name="(part._{slug})"></a>'
    # Search back up to 5 lines before the heading
    for j in range(max(0, heading_idx - 5), heading_idx):
        if lines[j].rstrip('\n') == target:
            return True
    return False


def process(text: str) -> str:
    lines = text.splitlines(keepends=True)
    # We'll rebuild the file, inserting anchors where needed.
    # Work backwards so that inserting lines doesn't shift indices.
    insertions = {}  # index -> list of lines to insert BEFORE lines[index]

    in_fence = False
    fence_marker = None

    for i, line in enumerate(lines):
        stripped = line.rstrip('\n')

        # Track fenced code blocks
        if not in_fence:
            m = re.match(r'^(`{3,}|~{3,})', stripped)
            if m:
                in_fence = True
                fence_marker = m.group(1)[:3]
                continue
        else:
            if stripped.startswith(fence_marker):
                in_fence = False
            continue

        # Only process headings outside fences
        hm = HEADING_RE.match(stripped)
        if hm:
            slug = hm.group(3)
            if not anchor_already_present(lines, i, slug):
                block = anchor_block(slug)
                # Ensure there's a blank line before our block if the
                # preceding line is non-blank.
                prefix = []
                if i > 0 and lines[i - 1].strip() != '':
                    prefix = ['\n']
                # The block itself already ends with '\n'; add a blank line
                # after the block so the heading is properly separated.
                suffix = ['\n']
                insertions[i] = prefix + block.splitlines(keepends=True) + suffix

    if not insertions:
        return text

    out = []
    for i, line in enumerate(lines):
        if i in insertions:
            out.extend(insertions[i])
        out.append(line)
    return ''.join(out)


def main():
    paths = sys.argv[1:]
    if not paths:
        print("Usage: add-scribble-anchors.py <file.md> [...]", file=sys.stderr)
        sys.exit(1)

    changed = 0
    for path in paths:
        with open(path, encoding='utf-8') as f:
            original = f.read()
        result = process(original)
        if result != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f'  modified: {path}')
            changed += 1
        else:
            print(f'  unchanged: {path}')

    print(f'\nDone: {changed} file(s) modified.')


if __name__ == '__main__':
    main()
