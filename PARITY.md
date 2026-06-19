# PARITY.md — Known gaps in the Jayret edition of DCIC

This file tracks known differences between the original Pyret DCIC textbook
and this Jayret-flavored fork. Items are grouped by severity and effort.

## Active gaps (require follow-up work)

### REPL outputs — 23 blocks remain unverifiable (irreducible)

`tools/verify-repl-outputs.py --all --in-place` processes all 70
`:::{.pyret-repl}` divs (59 with jayret/pyret inner blocks; 11 have
`python`-tagged inner blocks and are skipped).  Current status:

- **32 verified clean** — Jayret output matches the source.
- **4 input-only** — declaration-only divs, no output to verify.
- **23 unverifiable** — marked `<!-- TODO(verify-repl): … -->` in source
  (invisible in rendered HTML; locate with `grep -rn 'TODO(verify-repl)' src/`).

The 23 failures are irreducible with the current script design.  All fall
into one of two categories:

1. **Binding lives in prose** — `a1`, `a2`, `sl`, `L`, `hash-of`, etc. are
   defined in an HTML table or a prose fenced block outside any
   `:::{.pyret-repl}` div, so no prelude threading can reach them.
   Files: `unified-equality.md` (14), `unified-lists-memory.md` (4),
   `tables-to-lists.md` (1), `hash-set-kv.md` (2).

2. **Mutation checkpoint** — the same code appears multiple times with
   different expected outputs because the prose narrates a mutation between
   blocks (e.g. `a1 =~ a2;` before and after `a2 ! {balance 800}`).
   File: `unified-equality.md` (contributes to the 14 above).

The script now threads cumulative state: each verified block that succeeds
is prepended as a prelude for subsequent blocks in the same file.  Only
successful blocks are accumulated (failed blocks and input-only blocks are
not accumulated, to avoid corrupting the prelude with untranslated Pyret
syntax).

**To verify further**: these blocks can only be confirmed by running an
interactive Jayret session that includes the narrative setup code from
the prose.

### Untranslated code blocks (chapters 1–6 now cleared; others remain)

All `# TODO(pyret2jayret)` markers in chapters 1–6 and testing.md have been
resolved in the authenticity pass (commits fa41d0f–4ef3559):

- Evaluation trace snippets converted to plain code blocks with Jayret `{}` syntax
- Triple-backtick docstrings converted to `/* ... */` block comments
- Pyret pseudo-code skeletons (fun/end/cases) rewritten in Jayret switch/brace form

Remaining in other chapters: `grep -rn 'TODO(pyret2jayret)' src/` — use same
fix-or-defer judgment (re-tag evaluation traces as `pyret-deferred`; convert
teachable blocks to Jayret by hand).

### Chapter 27 — Reactor syntax deferred

`src/games-reactive.md` uses `reactor:` syntax in 5 blocks, tagged as
`` ```pyret-deferred ``.  These render with label
"Pyret (deferred in Jayret)" and link to the deferred-features registry
at `jayret-lang.github.io/docs/Deferred_from_Pyret.html`.

## Intentionally kept as Pyret

- `static/pyret.js` — original CodeMirror mode, still loaded for `pyret-deferred` blocks (Chapter 27)
- `{#anchor-id-in-Pyret}` heading anchors — kept for URL stability

## Already fixed

- **TOC + cross-reference anchor encoding mismatch (resolved 703ef52)**:
  `--include-fragments` is now ON in lychee. 110 prose `##slug` → `#slug`
  fixes; 37 heading-slug normalizations covering Scribble's `: ` → `--` and
  abbreviation encoding (`D-A-G` ↔ `DAG`, `C-S-V` ↔ `CSV`,
  `Data-Frame` ↔ `DataFrame`); 6 TOC href rewrites for tilde-encoded
  Scribble IDs (`~3a`, `~e2~80~99`); 2 lychee `--exclude` patterns
  (`%28elem._`, `struct.traverse.element`) for Scribble-only anchor forms
  with no plain-HTML equivalent.  Local lychee run clean over 5467 links.

- **REPL output reverification (34/65)**: ran
  `tools/verify-repl-outputs.py --all --in-place`; 34 self-contained
  blocks confirmed matching Jayret reality (no diffs), 5 declaration-only
  blocks skipped, 31 context-dependent blocks marked with TODO comments
  for follow-up.  Script fixes: strip trailing `;` before wrapping
  expressions in `to-repr()`; cleaner error-message formatting.
- **Jayret CodeMirror syntax highlighting**: new `static/jayret.js` mode
  (`switch`, `void`, `Object`, `@Check`, `assertEquals`, `->`, `//`, `/* */`, etc.);
  loaded alongside `pyret.js` in template; `pyret-repl` default lang updated to `"jayret"`
- **Inline `{.pyret}` → `{.jayret}` rename**: 2270 occurrences across 46 src/*.md files
  (29 fenced block openers + 2241 inline code-span attributes); applied via
  `tools/rebrand-pyret-class-md.py`
- `PyretReplInteraction` / `PyretRepl` CSS classes → renamed to
  `JayretReplInteraction` / `JayretRepl` in Lua filter + CSS
- `lang_label("pyret")` → `"Jayret"` in Lua filter
- All `pyret.org` / `code.pyret.org` URLs rewritten
- 643 prose mentions of "Pyret" → "Jayret" (2 anchor-ID exceptions)
- Booklet III retitled "From Jayret to Python"
- 718 / 792 (91%) code blocks translated to Jayret
- **Authenticity pass (chapters 1–6 + testing.md)**:
  - `fun`/`end`/`::`/`where:` prose → Jayret equivalents (ch3.3, 3.4)
  - `lam(r)...end` prose → arrow function `(r) -> ...` (ch4.1, 5.1)
  - `load-table:` deferred callout added to ch4.2
  - All TODO(pyret2jayret) blocks in ch1–6 resolved
  - `is`/`satisfies`/`raises` prose → `assertEquals`/`assertSatisfies`/`assertRaises`
  - `where:`/`check:` prose → `where { }`/`@Check void` in testing.md
  - `%(around)` approximate-test pattern → `assertRoughlyEquals`
  - `empty`/`link` variant names → `Empty`/`Link` in ch5.2, 5.3
  - `cases` → `switch` in ch5.2, 5.3, 6.1, 6.2
  - `pick-none`/`pick-some` → `Pick-none`/`Pick-some` in ch6.2
