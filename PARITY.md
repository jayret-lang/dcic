# PARITY.md — Known gaps in the Jayret edition of DCIC

This file tracks known differences between the original Pyret DCIC textbook
and this Jayret-flavored fork. Items are grouped by severity and effort.

## Active gaps (require follow-up work)

### CodeMirror highlighting is Pyret-keyword-aware, not Jayret

The loaded `static/pyret.js` CodeMirror mode tokenizes Pyret keywords
(`fun`, `end`, `where:`, `check:`, etc.).  After translation, code blocks
use Jayret syntax (`Object`, `void`, `switch`, `assertEquals`) that the
Pyret mode does not recognize, so blocks render unstyled or mis-styled.

**Fix**: Port `pyret.js` to a `jayret.js` CodeMirror mode (or extend the
Pyret mode), then rename the CSS class `{.pyret}` → `{.jayret}` throughout.
Coordinate with the `jayret-parley-vscode` TextMate grammar at
`jayret-parley-vscode/syntaxes/jayret.tmLanguage.json`.

**Deferred because**: touching `pyret.js` and all `{.pyret}` inline spans
is a large coordinated change; it blocks on having a Jayret grammar file.

### Inline `{.pyret}` attribute kept on translated code spans

Inline code spans like `` `expr`{.pyret} `` had their bodies translated
but kept the `{.pyret}` CSS class.  This class hooks into both the
CodeMirror highlighter (see above) and the Lua filter's `lang_label` lookup.

Renaming to `{.jayret}` is deferred until the CodeMirror mode is ready.

### REPL outputs not yet reverified

The 70 `:::{.pyret-repl}` output blocks were not regenerated in this
migration pass (Phase C of the plan).  Their content still reflects Pyret
outputs, which are numerically identical for arithmetic but may differ in
`to-repr` formatting for data types.

**Fix**: Run `python3 tools/verify-repl-outputs.py --all --in-place`
once the Jayret CLI is confirmed stable on this machine.

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

- `static/pyret.js` — CodeMirror mode (see above, deferred rename)
- `{.pyret}` CSS class on inline spans (deferred rename)
- `{#anchor-id-in-Pyret}` heading anchors — kept for URL stability

## Already fixed

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
