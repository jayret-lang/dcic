#!/usr/bin/env python3
"""
tools/rebrand-pyret-class-md.py
One-shot rename of Pyret class markers to Jayret in src/*.md.

Changes applied:
  1. Fenced block opener   ```pyret  →  ```jayret
     (does NOT touch ```pyret-deferred, ```pyret-repl, or any other hyphenated form)
  2. Inline code attribute  {.pyret}  →  {.jayret}
     (does NOT touch {.pyret-deferred}, {.pyret-repl}, etc. — different strings)

Usage:
  python3 tools/rebrand-pyret-class-md.py           # dry-run (prints counts only)
  python3 tools/rebrand-pyret-class-md.py --write   # apply changes in-place
"""

import argparse
import re
import sys
from pathlib import Path

# Matches a fenced code block opener like ```pyret or ```pyret   (trailing spaces ok)
# Negative lookahead prevents matching ```pyret-deferred, ```pyret-repl, etc.
FENCE_RE = re.compile(r'^(```+)pyret(?![-\w])([ \t]*)$', re.MULTILINE)

# Matches exactly {.pyret} — does NOT match {.pyret-deferred} etc.
# because those strings contain a hyphen before the closing brace.
ATTR_RE  = re.compile(r'\{\.pyret\}')


def process(text: str) -> tuple[str, int, int]:
    new_text = FENCE_RE.sub(r'\1jayret\2', text)
    fence_count = len(FENCE_RE.findall(text))
    new_text, attr_count = ATTR_RE.subn('{.jayret}', new_text)
    return new_text, fence_count, attr_count


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--write', action='store_true', help='Apply changes in-place (default: dry-run)')
    args = parser.parse_args()

    src_dir = Path(__file__).parent.parent / 'src'
    md_files = sorted(src_dir.glob('*.md'))
    if not md_files:
        print(f'No .md files found under {src_dir}', file=sys.stderr)
        sys.exit(1)

    total_files = 0
    total_fence = 0
    total_attr  = 0

    for path in md_files:
        original = path.read_text(encoding='utf-8')
        new_text, fence_count, attr_count = process(original)
        changed = (fence_count + attr_count) > 0
        if changed:
            total_files += 1
            total_fence  += fence_count
            total_attr   += attr_count
            print(f'  {path.name}: {fence_count} fence(s), {attr_count} attr(s)')
            if args.write:
                path.write_text(new_text, encoding='utf-8')

    mode = 'APPLIED' if args.write else 'DRY-RUN'
    print(f'\n[{mode}] {total_files} file(s), {total_fence} fence opener(s), {total_attr} inline attr(s)')
    if not args.write:
        print('Re-run with --write to apply.')


if __name__ == '__main__':
    main()
