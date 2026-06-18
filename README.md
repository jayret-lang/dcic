# DCIC — Jayret edition

A Jayret-flavored fork of the [DCIC textbook][upstream] ("A Data-Centric
Introduction to Computing"). Code samples have been ported from Pyret to
[Jayret][jayret], a Java-flavored surface syntax for the same runtime.

**Live site:** https://jayret-lang.github.io/dcic/

[upstream]: https://dcic-world.org/
[jayret]: https://jayret-lang.github.io/

## Build locally

```sh
python3 build.py --all
```

Renders every chapter from `src/*.md` into `docs/`. Requires Python 3.11+
with `pyyaml`, and `pandoc` on `PATH`.

Single chapter:

```sh
python3 build.py --file src/intro-python.md
```

By default the build invokes `nix run nixpkgs#pandoc --` (NixOS). To use
an installed pandoc, set `PANDOC`:

```sh
PANDOC=pandoc python3 build.py --all
```

## Deployment

`main` branch is built and published by `.github/workflows/deploy.yml`
on every push. The Pages source must be set to **GitHub Actions** in
repository Settings → Pages (legacy `main:/docs` mode is no longer used;
`docs/` is gitignored).

## Link checking

`.github/workflows/links.yml` runs [lychee][lychee] against the built
HTML on every push, every PR, and weekly on Mondays at 06:00 UTC. It
validates both URLs and `#fragment` anchors (the latter is the main
reason — heading-ID drift during the migration is the most likely
breakage). Run manually with the **Run workflow** button.

[lychee]: https://github.com/lycheeverse/lychee

## Repo layout

| Path | What it is |
|---|---|
| `src/*.md` | Source chapters (Pandoc Markdown). |
| `static/` | CSS, JS (CodeMirror modes incl. `jayret.js`), images. |
| `templates/dcic.html` | Pandoc HTML template. |
| `filters/*.lua` | Pandoc Lua filters (custom blocks, REPL rendering). |
| `book.yaml` | Chapter ordering, ToC structure. |
| `tools/` | One-shot maintenance scripts (translation, REPL verification). |
| `PARITY.md` | Tracks known gaps vs the upstream Pyret edition. |
| `HANDOFF.md` | Deeper background on the migration pipeline. |
