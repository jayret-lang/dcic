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

### Untranslated code blocks (72 remaining ```` ```pyret ```` blocks)

Translation failures — marked with `# TODO(pyret2jayret): <reason>`:

- **Evaluation trace snippets** (Conditionals_and_Booleans.md, etc.):
  blocks showing intermediate evaluation steps like `=> 45 * 10` are
  not valid Pyret programs and were correctly skipped.
- **Triple-backtick doc strings**: `fun f(): doc: \`\`\`...\`\`\` end`
  syntax causes a JSON parse error in the tokenizer; ~6 blocks in
  Conditionals_and_Booleans.md.
- **Other parse failures**: see `grep -rn 'TODO(pyret2jayret)' src/`.

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
