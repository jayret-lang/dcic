# PARITY.md — Known gaps in the Jayret edition of DCIC

This file tracks known differences between the original Pyret DCIC textbook
and this Jayret-flavored fork. Items are grouped by severity and effort.

## Active gaps (require follow-up work)

### REPL outputs — 31 blocks need context-aware verification

`tools/verify-repl-outputs.py --all --in-place` was run against all 70
`:::{.pyret-repl}` divs.  Result: **34 verified clean** (Jayret output
matches the source), **5 input-only** (declarations, no output to check),
**31 failed** because the script runs each block in isolation and many
blocks reference values bound by an earlier block in the same chapter
(e.g. `a1 == a2;` where `a1` was defined in a previous REPL block).

The 31 failed blocks are marked with `<!-- TODO(verify-repl): … -->`
HTML comments in the source (invisible in rendered HTML).  Locate with
`grep -rn 'TODO(verify-repl)' src/`.

**Breakdown of failures** (`src/unified-equality.md` accounts for 20 of
the 31 — most of those are in the "Equality in Python" subsection where
the code is tagged `jayret` but the displayed outputs are actually Python
REPL traces; a separate authenticity decision).

**Fix**: Teach the script to maintain per-chapter REPL state (feed all
blocks in a file as one sequential program); or manually verify the 31
remaining blocks against an interactive Jayret REPL.

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
