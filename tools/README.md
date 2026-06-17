# DCIC Migration Tools

Three scripts for the Pyret→Jayret migration of this textbook.

## Dependency

All three tools import from the sibling `jayret-docs` repo:

```
/home/artem/Dev/pyret/
├── jayret-docs/tools/pyret2jayret.mjs   ← AMD-shim translator (imported)
│                    prose-rebrand.py     ← regex tables (imported)
└── dcic-world.org/tools/                ← these scripts
```

Override with `JAYRET_DOCS_TOOLS_PATH` (JS) or `JAYRET_DOCS_TOOLS_PATH` (Python)
env var if the repos are not siblings.

## Scripts

### `pyret2jayret-md.mjs`

Translates `` ```pyret `` fenced blocks in Markdown files to `` ```jayret ``.
Imports `translateBlock` / `translateInline` from `jayret-docs`.

```bash
node tools/pyret2jayret-md.mjs --self-test
node tools/pyret2jayret-md.mjs --dry-run src/Naming_Values.md
node tools/pyret2jayret-md.mjs --in-place src/*.md
```

Flags: `--dry-run`, `--in-place`, `--check`, `--self-test`, `--verbose`.

Skips `pyret-deferred` fences (reactor syntax, Chapter 27).
Inline `` `expr`{.pyret} `` spans are also translated.

### `prose-rebrand-md.py`

Replaces `Pyret` → `Jayret` and `pyret.org` URLs in prose, skipping
fenced code blocks and inline code spans.

```bash
python3 tools/prose-rebrand-md.py --dry-run src/getting-started.md
python3 tools/prose-rebrand-md.py --in-place src/*.md
```

Flags: `--dry-run`, `--in-place`.

### `verify-repl-outputs.py`

Re-runs `::: {.pyret-repl}` input blocks through the Jayret CLI and
updates the paired `` ```output `` bodies with actual output.

```bash
# Warm-up + process all files
python3 tools/verify-repl-outputs.py --all --dry-run
python3 tools/verify-repl-outputs.py --file src/getting-started.md --in-place
```

Requires `node` and the Jayret CLI (`JAYRET_JS` env var, default:
`/home/artem/Dev/pyret/jayret-npm/jayret.js`).

On NixOS, set `LD_PRELOAD` to the path of `libuuid.so.1` (the script
does this automatically for the default Nix store path).
