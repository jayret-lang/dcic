# Session Handoff Document

## What This Project Is

A pipeline to rebuild the [DCIC book](https://dcic-world.org) ("A Data-Centric Introduction
to Computing") from a Pandoc Markdown intermediate, so the site can be edited and extended
in Markdown rather than Scribble (Racket). The output HTML is structurally identical to the
original Scribble-generated site.

**Live site**: https://jayret-lang.github.io/dcic/  
**GitHub repo**: https://github.com/jayret-lang/dcic  
**Local checkout**: `/home/artem/dev/pyret/dcic-world.org/`

---

## Current State

The pipeline is complete and all 80 pages pass structural round-trip verification. The GitHub
Pages site is live and serving correctly.

**What "structurally identical" means**: heading counts (h1–h4), exercise block counts
(`Incercise`, `Exercise`), code block counts (`sourceCodeWrapper`), and REPL interaction
counts (`PyretReplInteraction`) all match between original and rebuilt HTML, for every page.

---

## Repository Layout

```
/
├── src/             80 Pandoc Markdown sources (converted from original HTML)
├── docs/            Built HTML + assets — served by GitHub Pages
├── static/          Static assets (CSS, JS, images) copied into docs/ at build time
├── filters/
│   └── dcic-transforms.lua   Single Lua filter for Pandoc (the only one used)
├── templates/
│   └── dcic.html    Pandoc HTML5 template
├── book.yaml        Book structure: booklets → chapters → sections (with file names)
├── convert.py       HTML→Markdown converter (BeautifulSoup, 699 lines)
├── build.py         Build orchestrator: generates TOC, invokes Pandoc (390 lines)
├── index.html       Bootstrap splash page (root landing page)
├── css/dcic.css     CSS for splash page
├── DCIC_splash.png  Splash image
├── favicon.png      Favicon (also copied to docs/)
└── conversion-status.md   Pipeline documentation (detailed)
```

`filters/custom-blocks.lua`, `filters/repl-tables.lua`, `filters/margin-notes.lua` — legacy
files, superseded by `dcic-transforms.lua`. Not used.

---

## How to Run

**Dependencies** (NixOS environment):
```bash
nix run nixpkgs#python3Packages.pip -- install --target /tmp/pylibs beautifulsoup4 pyyaml
```

**Convert all HTML → Markdown** (only needed if re-converting from scratch):
```bash
python3 -c "
import sys, os; sys.path.insert(0, '/tmp/pylibs')
from convert import convert_file
src = '2025-08-27'
[convert_file(f'{src}/{f}') for f in sorted(os.listdir(src)) if f.endswith('.html')]
"
```
(The original HTML is in git history at `HEAD~3:2025-08-27/` — no longer in the working tree.)

**Build all pages**:
```bash
python3 build.py --all
```

**Build one page**:
```bash
python3 build.py --file src/getting-started.md
```

**Structural verification** (compare docs/ against original HTML from git):
```python
import sys, os, subprocess
sys.path.insert(0, '/tmp/pylibs')
from bs4 import BeautifulSoup

def check(orig_html, built_path):
    o = BeautifulSoup(orig_html, 'html.parser')
    with open(built_path) as f: b = BeautifulSoup(f, 'html.parser')
    failures = []
    for tag in ['h1','h2','h3','h4']:
        oc, bc = len(o.find_all(tag)), len(b.find_all(tag))
        if oc != bc: failures.append(f'{tag}: orig={oc} built={bc}')
    for cls in ['Incercise','Exercise','sourceCodeWrapper','PyretReplInteraction']:
        oc = len(o.find_all(class_=cls)); bc = len(b.find_all(class_=cls))
        if oc != bc: failures.append(f'{cls}: orig={oc} built={bc}')
    return failures

files = subprocess.check_output(
    ['git','show','HEAD~3','--name-only','--pretty=format:','--diff-filter=A']
).decode().strip().split('\n')
html_files = [f.replace('2025-08-27/','') for f in files if f.startswith('2025-08-27/') and f.endswith('.html')]
ok = bad = 0
for name in sorted(html_files):
    orig = subprocess.check_output(['git','show',f'HEAD~3:2025-08-27/{name}']).decode()
    failures = check(orig, f'docs/{name}')
    if failures: print(f'{name}: {failures}'); bad += 1
    else: ok += 1
print(f'{ok}/80 perfect')
```

---

## Pipeline Architecture

### convert.py — HTML → Markdown

Reads Scribble-generated HTML, outputs Pandoc Markdown to `src/`.

Key classes/functions:
- `Converter`: main class; dispatches on element type via `_tag()`
- `Converter._inline_children()`: handles mixed block/inline content inside `<p>` and
  `SIntrapara` divs. **Critical**: must NOT call `_paragraph()` (which strips) on `<p>`
  children — use `_inline_children(child)` directly to preserve trailing `\n` after code
  fences.
- `Converter._repl()`: converts `PyretReplInteraction` tables → `::: {.pyret-repl}` fenced
  div with ` ```pyret ` / ` ```output ` blocks.
- `Converter._custom_block()`: converts `Incercise`/`Exercise`/`Note`/etc. blockquotes →
  `::: {.do-now}` / `::: {.exercise}` / etc. fenced divs.
- `Converter._raw_html()`: wraps any complex element as `` ```{=html} `` passthrough.
- `RAW_HTML_CLASSES`: `{'HeapPart','HeapCode','EnvPart','ExprPart','HeapExpr', 'TwoColumn',
  'TwoColumnAsRows','RktBlk','SCodeFlow','SVerbatim'}` — treated as raw HTML islands.
  **`HeapExpr` must be in this set**: if it falls through to `_container()→_children_block()`,
  the `.strip()` in `_children_block` removes trailing `\n` from the closing ` ``` ` fence,
  causing the next text to concatenate onto it and corrupting Pandoc's parse.

### build.py — Markdown → HTML

- `load_book()` / `flat_file_list()` / `make_nav_index()`: book structure from `book.yaml`.
  - `flat_file_list` **skips chapters where `ch['file'] == booklet['file']`** — these are
    in-page sections of single-file booklets (currently only `booklet_intro.html`) and must
    not create duplicate nav entries.
- `build_tocset_html(current_file, ...)`: generates the full `<div class="tocset">` sidebar
  HTML. Writes it to a temp file and passes via `--include-before-body` (not `--variable`,
  because Pandoc HTML-escapes variable values).
- `build_file(md_path, ...)`: writes nav metadata to a temp YAML file for `--metadata-file`,
  then invokes Pandoc.
- Pandoc invoked as `nix run nixpkgs#pandoc --` with extensions:
  `markdown+fenced_divs+raw_html+tex_math_single_backslash+bracketed_spans+inline_code_attributes+smart`

### filters/dcic-transforms.lua

Returns `{ pass1, pass2 }`.

- **pass1** (topdown): converts Divs by class:
  - `.pyret-repl` → nested `PyretReplInteraction` tables
  - `.do-now`, `.exercise`, `.responsible-cs`, `.strategy`, `.note`, `.vscode-note`,
    `.world-def` → `<blockquote class="...">` blocks
  - `.centered` → `<div class="SCentered">`
  - Topdown traversal is **essential**: claiming `.pyret-repl` Divs in pass1 prevents
    pass2's `CodeBlock` handler from consuming the code blocks inside them.
- **pass2**: `CodeBlock` (fenced code → `sourceCodeWrapper` HTML), `Code` (inline pyret/
  python → `<span class="sourceCode">`), `Span` (margin-note, smaller).
- `blocks_to_html(blocks)`: walks blocks with `inner_filter` (same CodeBlock/Code/Span
  transforms) before calling `pandoc.write()`. **Required** so code inside custom blocks
  gets proper `data-lang` attributes.

### book.yaml — Book Structure

Three-level hierarchy: `booklets` → `chapters` → `sections`. Each node has `file`, `title`,
`number`. Used for:
1. `flat_file_list()` → linear ordering for prev/up/next nav
2. `build_tocset_html()` → sidebar with current-page highlighting

**Special case**: `booklet_intro` has chapters with `file: booklet_intro.html` (same as the
booklet) because all content is on one page. These are shown in the sidebar but excluded from
nav ordering.

---

## Git History

```
HEAD     8f61633  Fix empty TOC sidebar on booklet pages
HEAD~1   d5ca07b  Fix part_* pages being empty
HEAD~2   d46e9b7  Convert sources to Markdown; serve built site from docs/
HEAD~3   919538a  Add HTML→Markdown conversion harness
HEAD~4   554164b  Add original DCIC site snapshot (2025-08-27)
```

The original HTML is recoverable from `HEAD~4:2025-08-27/`.

---

## Bugs Fixed (for context)

1. **SIntrapara + `<p>` child stripping** — `_inline_children` called `_paragraph()` on `<p>`
   children which `.strip()`s, removing trailing `\n` after code fences. Adjacent text then
   concatenated onto ` ``` ` producing e.g. `` ```These are unsatisfying... `` which Pandoc
   misread as a new code block language, swallowing all following content. Fixed: `elif
   child.name == 'p': parts.append(self._inline_children(child))`.

2. **`HeapExpr` container stripping** — `HeapExpr` divs went through `_container →
   _children_block`, which strips results, removing trailing `\n` from `{=html}` fences.
   Next text concatenated as `` ```Note that the entry for... ``. Fixed: add `'HeapExpr'`
   to `RAW_HTML_CLASSES`.

3. **`_is_toc_table` over-dropping** — All tables with `class="toclink"` links were dropped.
   Correct for small inline sub-TOC tables in chapters, but also dropped the entire content
   table of `part_*` pages (which IS a toclink table). Fixed: remove the check; emit all
   non-REPL tables as raw HTML.

4. **`booklet_intro` empty sidebar** — `chapters: []` meant nothing shown under "Introduction"
   in sidebar. Fixed: add `Overview` and `Acknowledgments` chapters (same file) to
   `book.yaml`; skip same-file chapters in `flat_file_list`; use `tocviewlink` (not
   `tocviewselflink`) for same-file chapter entries.

---

## Known Remaining Issues / Possible Next Work

- **No GitHub Actions CI**: builds require the local NixOS environment (`nix run
  nixpkgs#pandoc`). A CI workflow would need either a nix action or pre-installing pandoc.
- **`src/` and `docs/` are both committed**: this is a deliberate trade-off for simple GitHub
  Pages deployment (no CI needed), but it means the repo is large and commits touch many
  files on each rebuild. Could move to a CI-only build in the future.
- **Anchor link correctness**: cross-file `#section-id` links are normalized from Scribble's
  `%28part._...%29` encoding, but not exhaustively validated.
- **`index.html` splash page**: the Bootstrap landing page at `docs/index.html` is the
  Scribble-generated TOC page (from `src/index.md`), not the Bootstrap splash. The Bootstrap
  splash (`index.html` at repo root) is also copied to `docs/` but is overwritten by the
  Pandoc-built `index.html`. These two should be reconciled if a custom splash is wanted.
- **MathJax version**: the page uses an old MathJax 2.x CDN-loaded version with a local
  stub `MathJax.js@config=default`. Works but is outdated.
- **Pyret code highlighting**: the `data-lang="pyret"` attribute on code blocks is wired for
  `hilite.js` to do client-side syntax highlighting, matching the original. No changes needed.
