#!/usr/bin/env python3
"""
loosen-lists.py — one-shot tool to make all Markdown lists "loose".

Pandoc emits <li>text</li> for tight lists (no blank lines between items)
and <li><p>text</p></li> for loose lists.  scribble.css only styles the
latter (via `p { margin: 1em 0 }`), so tight lists render with no vertical
breathing room.

This script inserts a blank line between consecutive list items, turning
every tight list into a loose one.  Fenced code blocks are left untouched.
The transformation is idempotent: running it twice is a no-op.

Usage:
    python3 tools/loosen-lists.py src/*.md
    python3 tools/loosen-lists.py src/getting-started.md   # single file test
"""

import re
import sys


# Matches the start of a list item at any indent level.
# group(1) = leading whitespace, group(2) = marker ("- " or "N. ")
ITEM_RE = re.compile(r'^(\s*)(- |\* |\d+\. )')
# Matches a fenced code block opening/closing (``` or ~~~)
FENCE_RE = re.compile(r'^(`{3,}|~{3,})')


def loosen(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out = []
    in_fence = False
    fence_marker = None

    # State for list tracking:
    # last_item_indent: indent level of the most recent list item seen
    #   (reset to -1 when a blank line appears)
    # prev_was_blank: True if the previous emitted line was blank
    last_item_indent = -1
    prev_was_blank = True  # start of file is treated as preceded by blank

    for line in lines:
        stripped = line.rstrip('\n')

        # --- Fenced code block tracking ---
        fence_m = FENCE_RE.match(stripped)
        if fence_m:
            if not in_fence:
                in_fence = True
                fence_marker = fence_m.group(1)[:3]
            elif stripped.startswith(fence_marker):
                in_fence = False
            out.append(line)
            prev_was_blank = False
            continue

        if in_fence:
            out.append(line)
            prev_was_blank = False
            continue

        # --- Blank line ---
        if stripped == '':
            last_item_indent = -1
            out.append(line)
            prev_was_blank = True
            continue

        # --- List item ---
        item_m = ITEM_RE.match(line)
        if item_m:
            indent = len(item_m.group(1))
            if (not prev_was_blank) and (last_item_indent == indent):
                # Same-level item immediately after a previous item (or its
                # continuation) — insert the missing blank line.
                out.append('\n')
            last_item_indent = indent
            out.append(line)
            prev_was_blank = False
            continue

        # --- Non-blank, non-item line ---
        # Could be prose or a continuation of a list item.
        # If it's a continuation (indent > last_item_indent when last_item_indent >= 0),
        # we keep last_item_indent so that the next sibling item can still be
        # detected as needing a blank line.
        if last_item_indent >= 0:
            content_start = last_item_indent + 2  # "- " is 2 chars
            line_indent = len(line) - len(line.lstrip())
            if line_indent >= content_start:
                # Continuation line — preserve last_item_indent
                out.append(line)
                prev_was_blank = False
                continue
        # Regular prose — reset list tracking
        last_item_indent = -1
        out.append(line)
        prev_was_blank = False

    return ''.join(out)


def main():
    paths = sys.argv[1:]
    if not paths:
        print("Usage: loosen-lists.py <file.md> [...]", file=sys.stderr)
        sys.exit(1)

    changed = 0
    for path in paths:
        with open(path, encoding='utf-8') as f:
            original = f.read()
        result = loosen(original)
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
