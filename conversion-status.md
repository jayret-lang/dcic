# DCIC HTML→Markdown Conversion: Status

## Goal

Rebuild the [Data-Centric Introduction to Computing](https://dcic-world.org) book from a
Scribble-generated HTML snapshot (`2025-08-27/`) through a Pandoc Markdown intermediate,
producing HTML output that is structurally identical to the originals.

---

## Current State: Complete

All **80 source files** have been converted and rebuilt. Every file passes a structural
round-trip check (see Verification below).

---

## Pipeline

```
2025-08-27/*.html  →  convert.py  →  src/*.md  →  build.py + pandoc  →  build/*.html
```

| File | Role | Size |
|---|---|---|
| `convert.py` | HTML→Markdown converter (BeautifulSoup) | 699 lines |
| `build.py` | Build orchestrator; generates TOC sidebar and nav; invokes Pandoc | 390 lines |
| `filters/dcic-transforms.lua` | Pandoc Lua filter: fenced divs → Scribble HTML blocks | 229 lines |
| `templates/dcic.html` | Pandoc HTML5 template reconstructing full page structure | 69 lines |
| `book.yaml` | Complete book structure (booklets → chapters → sections) for nav/TOC | — |

### Key dependencies

- **Python 3** with `beautifulsoup4` (installed to `/tmp/pylibs`) and `pyyaml`
- **Pandoc** via `nix run nixpkgs#pandoc`

### Invoking the build

```bash
# Convert all HTML to Markdown
python3 -c "
import sys, os; sys.path.insert(0, '/tmp/pylibs')
from convert import convert_file
[convert_file(f'2025-08-27/{f}') for f in sorted(os.listdir('2025-08-27')) if f.endswith('.html')]
"

# Build all HTML pages
python3 build.py --all

# Build a single file
python3 build.py --file src/getting-started.md
```

---

## What the converter handles

| Source construct | Markdown representation |
|---|---|
| Fenced code blocks (Pyret, Python, output) | ` ```pyret ` / ` ```python ` / ` ```output ` |
| Inline code with language | `` `code`{.pyret} `` |
| REPL interactions (`PyretReplInteraction`) | `::: {.pyret-repl}` fenced div |
| Exercise / Do Now / Strategy / Note blocks | `::: {.exercise}` etc. fenced divs |
| Margin notes (`refelem`) | `[text]{.margin-note}` bracketed spans |
| Memory diagrams (`HeapExpr`, `EnvPart`, `HeapPart`, …) | Raw HTML passthrough (`{=html}`) |
| Two-column layouts, TOC tables, etc. | Raw HTML passthrough |
| Math (`\(...\)`, `\[...\]`) | Preserved as-is via `tex_math_single_backslash` |
| Navigation (prev/up/next) | Pandoc metadata file → template variables |
| TOC sidebar | Python-generated HTML → `--include-before-body` |

---

## Verification

Structural round-trip check compares element counts for headings (h1–h4), exercise blocks
(`Incercise`, `Exercise`), code wrappers (`sourceCodeWrapper`), and REPL tables
(`PyretReplInteraction`) between each original and rebuilt file.

**Result: 80/80 perfect matches.**

---

## Bugs found and fixed

### 1. `SIntrapara` + `<p>` child stripping

**Symptom:** 40–60% of content missing from large chapters (`processing-lists`,
`intro-tabular-data`, `games-reactive`). All headings and exercises after the first
few disappeared.

**Root cause:** `_inline_children()` processes `SIntrapara` divs recursively. When a
`SIntrapara` contained a `<p>` child (itself containing a code block), the converter
called `_paragraph()` on it, which `.strip()`s the result. This removed the trailing
`\n` after the closing ` ``` ` fence of the code block. The next adjacent text then
concatenated directly: `` ```These are unsatisfying... ``. Pandoc read "These" as a
code-block language tag and swallowed all subsequent content until the next ` ``` `.

**Fix:** Added an `elif child.name == 'p'` branch in `_inline_children` that recurses
with `_inline_children(child)` instead of calling `_paragraph()`, preserving the
trailing newline.

### 2. `HeapExpr` container stripping

**Symptom:** 4 files (`Naming_Values`, `mutable-lists`, `unified-equality`,
`unified-lists-memory`) had 1–4 missing exercise/REPL blocks each.

**Root cause:** `HeapExpr` divs (wrapping `EnvPart` + `HeapPart` memory diagrams) were
not in `RAW_HTML_CLASSES`. They went through `_container()` → `_children_block()`,
which calls `.strip()` on each child result. This removed the trailing `\n` from the
inner `{=html}` block's closing ` ``` ` fence. The immediately following SIntrapara
text then produced `` ```Note that the entry for... `` on one line — again, Pandoc
read "Note" as a language tag, opening a phantom code block that consumed the
following exercise.

**Fix:** Added `'HeapExpr'` to `RAW_HTML_CLASSES` so the entire `HeapExpr` div is
emitted as a single `{=html}` raw block (with a proper trailing `\n`) rather than
being decomposed into its children.

### 3. Earlier infrastructure bugs (resolved)

- `lxml` not available → switched to `html.parser`
- `pandoc` not in PATH → `nix run nixpkgs#pandoc` invocation
- TOC sidebar being HTML-escaped → switched from `--variable` to `--include-before-body` temp file
- Filter ordering: inline Pyret code inside exercises lacked `data-lang` → merged three
  separate Lua filters into one (`dcic-transforms.lua`) with `inner_filter` applied
  before `pandoc.write()`
- REPL code blocks consumed by `CodeBlock` handler → topdown traversal in pass1 converts
  `.pyret-repl` Divs to raw HTML before pass2's `CodeBlock` sees their children

---

## Remaining limitations

- **Raw HTML fidelity:** Memory diagrams, two-column layouts, and similar complex
  structures are preserved as verbatim raw HTML blobs. They render correctly but are
  not markdownified.
- **Anchor links:** Cross-file `#section-anchor` links are normalized but not exhaustively
  validated.
- **Index page (`index.html`):** Not built by the pipeline (no `.md` source); the
  original is used directly.
