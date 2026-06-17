#!/usr/bin/env node
/**
 * pyret2jayret-md.mjs — translate Pyret fenced blocks in DCIC Markdown files.
 *
 * Imports the CST walker from the sibling jayret-docs tools directory.
 * (Assumes /home/artem/Dev/pyret/{jayret-docs,dcic-world.org}/ are siblings;
 *  override with env JAYRET_DOCS_TOOLS_PATH if layout differs.)
 *
 * Usage:
 *   node tools/pyret2jayret-md.mjs [--dry-run] [--in-place] [--check]
 *                                   [--self-test] [--verbose] <file.md> [...]
 */

import { readFileSync, writeFileSync } from 'fs';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const JAYRET_DOCS_TOOLS = process.env.JAYRET_DOCS_TOOLS_PATH
  || resolve(__dirname, '../../jayret-docs/tools/pyret2jayret.mjs');

const { translateBlock, translateInline } = await import(JAYRET_DOCS_TOOLS);

// ---------------------------------------------------------------------------
// CLI flags
// ---------------------------------------------------------------------------
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const IN_PLACE = args.includes('--in-place');
const CHECK = args.includes('--check');
const SELF_TEST = args.includes('--self-test');
const VERBOSE = args.includes('--verbose');
const files = args.filter(a => !a.startsWith('--'));

// ---------------------------------------------------------------------------
// Self-test — port 14 canonical cases from jayret-docs translator
// ---------------------------------------------------------------------------
if (SELF_TEST) {
  // Mirror the 14 cases from jayret-docs/tools/pyret2jayret.mjs --self-test,
  // using regex matching so we stay in sync with the same translator.
  const cases = [
    { name: 'no-ann let-decl',    src: `x = 5`,                                        want: /^x = 5;?\s*$/ },
    { name: 'ann let-decl',       src: `x :: Number = 5`,                              want: /int x = 5;/ },
    { name: 'fun w/ return',      src: `fun square(n :: Number) -> Number:\n  n * n\nend`, want: /int square\(int n\)/ },
    { name: 'if/else',            src: `fun abs(n):\n  if n < 0: (0 - n) else: n end\nend`, want: /if \(n < 0\)/ },
    { name: 'cases → switch',     src: `cases(List) lst:\n  | empty => 0\n  | link(f, r) => f\nend`, want: /switch \(lst\).*Empty.*Link\(f, r\)/s },
    { name: 'check block',        src: `check "math":\n  1 + 1 is 2\nend`,             want: /@Check void math\(\).*assertEquals\(1 \+ 1, 2\)/s },
    { name: 'lambda',             src: `lam(n :: Number): n * 2 end`,                  want: /\(int n\) -> n \* 2/ },
    { name: 'data',               src: `data Shape:\n  | circle(r :: Number)\n  | rectangle(w :: Number, h :: Number)\nend`, want: /data Shape \{.*Circle\(int r\);.*Rectangle\(int w, int h\);/s },
    { name: 'list literal',       src: `[list: 1, 2, 3]`,                              want: /\[1, 2, 3\]/ },
    { name: 'comments preserved', src: `# a comment\nx = 1`,                           want: /\/\/ a comment/ },
    { name: 'for-each',           src: `for each(x from xs): print(x) end`,            want: /for \(x : xs\) \{/ },
    { name: 'and→&&',             src: `check:\n  (true and false) is false\nend`,     want: /true && false/ },
    { name: 'use context',        src: `use context essentials2021\n\nx = 5`,          want: /use context|TODO|essentials2021/ },
    { name: 'provide *',          src: `provide *\n\nx = 1`,                           want: /provide \*|implicitly|Jayret/ },
  ];

  let pass = 0; let fail = 0;
  for (const c of cases) {
    const r = translateBlock(c.src);
    if (!r.ok) { console.error(`FAIL  ${c.name}: ${r.err}`); fail++; continue; }
    if (!c.want.test(r.out)) {
      console.error(`FAIL  ${c.name}\n      got: ${JSON.stringify(r.out.slice(0, 200))}\n      want match: ${c.want}`);
      fail++; continue;
    }
    console.log(`ok    ${c.name}`); pass++;
  }
  console.log(`\nSelf-test: ${pass}/${cases.length} passed${fail ? ' ← FAILURES ABOVE' : ''}`);
  process.exit(fail > 0 ? 1 : 0);
}

// ---------------------------------------------------------------------------
// Per-file translation
// ---------------------------------------------------------------------------

/**
 * Translate all Pyret fenced blocks (and inline spans) in a Markdown string.
 * Returns { out, stats }.
 *
 * Handles:
 *   1. ```pyret ... ``` — translate body
 *   2. ```pyret-deferred ... ``` — skip (leave as-is)
 *   3. `inline`{.pyret} — translate inline body
 *   4. :::: {.pyret-repl} divs — translate inner ```pyret block, leave output
 *   5. ```python, ```output, plain ``` — skip
 */
function translateMarkdown(src) {
  const lines = src.split('\n');
  const out = [];
  const stats = { total: 0, ok: 0, failed: 0, failedBlocks: [] };

  let i = 0;
  while (i < lines.length) {
    const line = lines[i];

    // Detect fenced code block opener: optional indent + ``` + optional space + lang
    const fenceM = line.match(/^(\s*)(```+) ?(\S*)(.*)$/);
    if (fenceM) {
      const indent = fenceM[1];
      const ticks = fenceM[2];
      const lang = fenceM[3];
      const rest = fenceM[4];

      if (lang === 'pyret' && rest === '') {
        // Collect body lines
        const bodyLines = [];
        i++;
        while (i < lines.length && !lines[i].startsWith(indent + ticks)) {
          bodyLines.push(lines[i]);
          i++;
        }
        const closeLine = lines[i] || (indent + ticks);
        i++;

        stats.total++;
        const body = bodyLines.join('\n');
        const r = translateBlock(body);
        if (r.ok) {
          stats.ok++;
          out.push(indent + ticks + 'jayret');
          for (const l of r.out.split('\n')) out.push(l);
          out.push(closeLine);
        } else {
          stats.failed++;
          stats.failedBlocks.push({ err: r.err, body: body.slice(0, 120) });
          if (VERBOSE) {
            process.stderr.write(`  TODO(pyret2jayret): ${r.err}\n`);
          }
          // Emit original with a TODO comment
          out.push(indent + ticks + 'pyret');
          out.push(`${indent}# TODO(pyret2jayret): ${r.err}`);
          for (const l of bodyLines) out.push(l);
          out.push(closeLine);
        }
        continue;
      }

      if (lang === 'pyret-deferred' || lang === '') {
        // Skip entirely — pass through unchanged
        out.push(line);
        i++;
        while (i < lines.length && !lines[i].startsWith(indent + ticks)) {
          out.push(lines[i]);
          i++;
        }
        if (i < lines.length) { out.push(lines[i]); i++; }
        continue;
      }

      // All other fences (python, output, jayret, etc.) — pass through
      out.push(line);
      i++;
      while (i < lines.length && !lines[i].startsWith(indent + ticks)) {
        out.push(lines[i]);
        i++;
      }
      if (i < lines.length) { out.push(lines[i]); i++; }
      continue;
    }

    // Inline `code`{.pyret} spans — translate each occurrence on the line.
    // Pattern: `body`{.pyret}  — note: body may contain backslashes but not backticks.
    const translatedLine = line.replace(/`([^`]+)`\{\.pyret\}/g, (match, body) => {
      const r = translateInline(body);
      if (r.ok) return `\`${r.out}\`{.pyret}`;
      return match; // leave unchanged on failure
    });

    out.push(translatedLine);
    i++;
  }

  return { out: out.join('\n'), stats };
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

if (files.length === 0 && !SELF_TEST) {
  console.error('Usage: node tools/pyret2jayret-md.mjs [--dry-run|--in-place|--check] <file.md> ...');
  process.exit(1);
}

let totalOk = 0; let totalFailed = 0; let totalTotal = 0;
let anyChanged = false;

for (const f of files) {
  const src = readFileSync(f, 'utf8');
  const { out, stats } = translateMarkdown(src);
  totalTotal += stats.total;
  totalOk += stats.ok;
  totalFailed += stats.failed;

  const changed = out !== src;
  if (changed) anyChanged = true;

  const pct = stats.total > 0 ? Math.round(100 * stats.ok / stats.total) : 100;
  if (VERBOSE || stats.failed > 0) {
    const tag = stats.failed > 0 ? `  [${pct}% ok, ${stats.failed} failed]` : `  [${pct}% ok]`;
    console.log(`${f}:${tag}`);
    if (VERBOSE) {
      for (const fb of stats.failedBlocks) {
        console.log(`    failed: ${fb.err}`);
        console.log(`    body:   ${fb.body.replace(/\n/g, ' ↵ ')}`);
      }
    }
  } else {
    console.log(`${f}: ${stats.ok}/${stats.total} blocks translated`);
  }

  if (IN_PLACE && changed) {
    writeFileSync(f, out, 'utf8');
  } else if (DRY_RUN && changed) {
    // Show a very brief diff summary
    const origLines = src.split('\n').length;
    const outLines = out.split('\n').length;
    console.log(`  (dry-run) would write ${outLines} lines (was ${origLines})`);
  }
}

const totalPct = totalTotal > 0 ? Math.round(100 * totalOk / totalTotal) : 100;
console.log(`\nTotal: ${totalOk}/${totalTotal} blocks translated (${totalPct}%), ${totalFailed} failed`);

if (CHECK && anyChanged) {
  process.exit(1); // signal that files would change
}
