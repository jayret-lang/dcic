#!/usr/bin/env python3
"""Normalize TOC hrefs in src/*.md from Scribble dot-encoding to slug-form.

Scribble-generated TOC tables use dot-encoded anchors like:
  href="page.html#%28part._.A_.First_.Example%29"

The <a name> anchors added by add-scribble-anchors.py use slug-form:
  <a name="(part._A-First-Example)">

Decode rule: inside (part._.X), replace underscores with hyphens and
strip dots from X, yielding (part._A-First-Example).

Run without args for a dry-run (prints per-file change counts).
Run with --write to apply changes in place.
"""

import re
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent / "src"

# Matches %28part._.BODY%29 where BODY is the dot-encoded section title.
# Capture group 1 is the BODY.
DOT_PATTERN = re.compile(r"%28part\._\.([^%]+)%29")


def decode_body(body: str) -> str:
    """Convert dot-encoded body to slug: replace _ with - then strip dots."""
    return body.replace("_", "-").replace(".", "")


def normalize_file(path: Path, write: bool) -> int:
    text = path.read_text(encoding="utf-8")
    changes = 0

    def replacer(m: re.Match) -> str:
        nonlocal changes
        body = m.group(1)
        slug = decode_body(body)
        changes += 1
        return f"%28part._{slug}%29"

    new_text = DOT_PATTERN.sub(replacer, text)

    if write and changes:
        path.write_text(new_text, encoding="utf-8")

    return changes


def main() -> None:
    write = "--write" in sys.argv
    total = 0
    for md in sorted(SRC_DIR.glob("*.md")):
        n = normalize_file(md, write)
        if n:
            print(f"  {md.name}: {n} href(s) {'rewritten' if write else 'to rewrite'}")
            total += n
    print(f"\nTotal: {total} href(s) {'rewritten' if write else 'would be rewritten'}")
    if not write:
        print("(dry-run — pass --write to apply)")


if __name__ == "__main__":
    main()
