#!/usr/bin/env python3
"""
build.py – Build DCIC HTML output from Markdown sources.

Usage:
    python3 build.py [--file <chapter.md>] [--all] [--clean]

Options:
    --all           Build every chapter (default if no --file given)
    --file FILE     Build a single chapter .md file
    --clean         Delete build/ output before building
    --src SRC       Source directory (default: src/)
    --out OUT       Output directory (default: build/)
"""

import sys, os, re, shutil, subprocess, argparse, html
sys.path.insert(0, '/tmp/pylibs')
import yaml

ROOT      = os.path.dirname(os.path.abspath(__file__))
SRC_DIR   = os.path.join(ROOT, 'src')
OUT_DIR   = os.path.join(ROOT, 'docs')
ORIG_DIR  = os.path.join(ROOT, 'static')
TMPL_DIR  = os.path.join(ROOT, 'templates')
FILT_DIR  = os.path.join(ROOT, 'filters')
BOOK_YAML = os.path.join(ROOT, 'book.yaml')

PANDOC    = os.environ.get('PANDOC', 'nix run nixpkgs#pandoc --').split()

# ---------------------------------------------------------------------------
# Book structure helpers
# ---------------------------------------------------------------------------

def load_book():
    with open(BOOK_YAML) as f:
        return yaml.safe_load(f)

def flat_file_list(book):
    """Return ordered list of dicts: {file, title, number, up, parent_booklet}."""
    entries = [{'file': 'index.html', 'title': book['title'], 'number': '', 'up': None}]
    for booklet in book['booklets']:
        bl = {
            'file':   booklet['file'],
            'title':  booklet['title'],
            'number': booklet['number'],
            'up':     'index.html',
            'booklet_id': booklet['id'],
        }
        entries.append(bl)
        for ch in booklet.get('chapters', []):
            # Skip chapters that live in the same file as the booklet
            # (e.g. booklet_intro sections — in-page anchors, not separate files)
            if ch['file'] == booklet['file']:
                continue
            ch_entry = {
                'file':   ch['file'],
                'title':  ch['title'],
                'number': ch['number'],
                'up':     booklet['file'],
                'booklet_id': booklet['id'],
            }
            entries.append(ch_entry)
            for sec in ch.get('sections', []):
                entries.append({
                    'file':   sec['file'],
                    'title':  sec['title'],
                    'number': sec['number'],
                    'up':     ch['file'],
                    'booklet_id': booklet['id'],
                })
    return entries

def make_nav_index(flat):
    """Map filename → {prev, up, next}."""
    nav = {}
    for i, entry in enumerate(flat):
        nav[entry['file']] = {
            'prev': flat[i-1]['file'] if i > 0 else None,
            'up':   entry.get('up'),
            'next': flat[i+1]['file'] if i < len(flat)-1 else None,
        }
    return nav

# ---------------------------------------------------------------------------
# TOC HTML generator
# ---------------------------------------------------------------------------

def esc(s):
    return html.escape(str(s))

def build_tocset_html(current_file, book, flat, nav_index):
    """Generate the full div.tocset sidebar HTML for a given page."""

    lines = ['<div class="tocset"><div class="tocview">']

    # Identify current booklet
    current_booklet = None
    for e in flat:
        if e['file'] == current_file and 'booklet_id' in e:
            current_booklet = next(
                (b for b in book['booklets'] if b['id'] == e['booklet_id']), None
            )
            break

    # Does the current booklet have chapters with their own files?
    has_nav_chapters = current_booklet and any(
        ch['file'] != current_booklet['file']
        for ch in current_booklet.get('chapters', [])
    )

    # Book list: expand only when on a booklet page whose booklet has no nav chapters
    # (e.g. booklet_intro.html — showing the book list is the best we can offer).
    expand_book_list = (
        current_booklet is not None and
        current_file == current_booklet['file'] and
        not has_nav_chapters
    )

    # --- Top-level: whole book ---
    lines.append(
        '<div class="tocviewlist tocviewlisttopspace">'
        '<div class="tocviewtitle">'
        '<table cellspacing="0" cellpadding="0"><tr>'
        '<td style="width: 1em;"><a href="javascript:void(0);" title="Expand/Collapse" '
        'class="tocviewtoggle" onclick="TocviewToggle(this,&quot;tocview_0&quot;);">'
        + ('&#9660;' if expand_book_list else '&#9658;') +
        '</a></td>'
        '<td></td>'
        '<td><a href="index.html" class="tocviewlink" data-pltdoc="x">'
        'A Data-&#8203;Centric Introduction to Computing</a></td>'
        '</tr></table></div>'
        '<div class="tocviewsublisttop" style="display: ' +
        ('block' if expand_book_list else 'none') + ';" id="tocview_0">'
        '<table cellspacing="0" cellpadding="0">'
    )
    for booklet in book['booklets']:
        link_class = 'tocviewselflink' if booklet['file'] == current_file \
                     else 'tocviewlink'
        lines.append(
            f'<tr><td align="right">{esc(booklet["number"])}&nbsp;</td>'
            f'<td><a href="{esc(booklet["file"])}" class="{link_class}" data-pltdoc="x">'
            f'{esc(booklet["title"])}</a></td></tr>'
        )
    lines.append('</table></div></div>')

    toc_id = 1
    if current_booklet:
        # Find current chapter (skip same-file/inline chapters)
        current_chapter = None
        for ch in current_booklet.get('chapters', []):
            if ch['file'] == current_booklet['file']:
                continue
            if ch['file'] == current_file or any(
                s['file'] == current_file for s in ch.get('sections', [])
            ):
                current_chapter = ch
                break

        chapter_sections = current_chapter.get('sections', []) if current_chapter else []
        has_sections = bool(chapter_sections)
        is_on_booklet = current_file == current_booklet['file']
        is_leaf_chapter = (current_chapter is not None and
                           not has_sections and
                           current_chapter['file'] == current_file)
        current_sec = next((s for s in chapter_sections if s['file'] == current_file), None)
        is_section_page = current_sec is not None

        # Booklet chapter list: expanded when on a booklet page (with nav chapters) or a leaf chapter.
        # Class is tocviewsublistbottom when it's the last panel (booklet page), tocviewsublist otherwise.
        expand_bl = (is_on_booklet and has_nav_chapters) or is_leaf_chapter
        bl_is_bottom = is_on_booklet  # nothing more below on any booklet page
        bl_class = 'tocviewsublistbottom' if bl_is_bottom else 'tocviewsublist'
        bl_arrow = '&#9660;' if expand_bl else '&#9658;'

        link_class = 'tocviewselflink' if current_booklet['file'] == current_file \
                     else 'tocviewlink'
        lines.append(
            '<div class="tocviewlist">'
            '<table cellspacing="0" cellpadding="0"><tr>'
            f'<td style="width: 1em;"><a href="javascript:void(0);" title="Expand/Collapse" '
            f'class="tocviewtoggle" onclick="TocviewToggle(this,&quot;tocview_{toc_id}&quot;);">{bl_arrow}</a></td>'
            f'<td>{esc(current_booklet["number"])}&nbsp;</td>'
            f'<td><a href="{esc(current_booklet["file"])}" class="{link_class}" data-pltdoc="x">'
            f'{esc(current_booklet["title"])}</a></td>'
            '</tr></table>'
            f'<div class="{bl_class}" style="display: {"block" if expand_bl else "none"};" id="tocview_{toc_id}">'
            '<table cellspacing="0" cellpadding="0">'
        )
        toc_id += 1
        for ch in current_booklet.get('chapters', []):
            same_file = ch['file'] == current_booklet['file']
            ch_class = 'tocviewlink' if same_file else \
                       ('tocviewselflink' if ch['file'] == current_file else 'tocviewlink')
            lines.append(
                f'<tr><td align="right">{esc(ch["number"])}&nbsp;</td>'
                f'<td><a href="{esc(ch["file"])}" class="{ch_class}" data-pltdoc="x">'
                f'{esc(ch["title"])}</a></td></tr>'
            )
        lines.append('</table></div></div>')

        # --- Current chapter section list (only when chapter has sections) ---
        if current_chapter and has_sections:
            # tocviewsublistbottom when there's no on-this-page panel below (chapter/part pages);
            # tocviewsublist when on a section page (on-this-page panel follows).
            sec_list_class = 'tocviewsublist' if is_section_page else 'tocviewsublistbottom'
            ch_class = 'tocviewselflink' if current_chapter['file'] == current_file \
                       else 'tocviewlink'
            lines.append(
                '<div class="tocviewlist">'
                '<table cellspacing="0" cellpadding="0"><tr>'
                f'<td style="width: 1em;"><a href="javascript:void(0);" title="Expand/Collapse" '
                f'class="tocviewtoggle" onclick="TocviewToggle(this,&quot;tocview_{toc_id}&quot;);">&#9660;</a></td>'
                f'<td>{esc(current_chapter["number"])}&nbsp;</td>'
                f'<td><a href="{esc(current_chapter["file"])}" class="{ch_class}" data-pltdoc="x">'
                f'{esc(current_chapter["title"])}</a></td>'
                '</tr></table>'
                f'<div class="{sec_list_class}" style="display: block;" id="tocview_{toc_id}">'
                '<table cellspacing="0" cellpadding="0">'
            )
            toc_id += 1
            for sec in chapter_sections:
                sec_class = 'tocviewselflink' if sec['file'] == current_file else 'tocviewlink'
                lines.append(
                    f'<tr><td align="right">{esc(sec["number"])}&nbsp;</td>'
                    f'<td><a href="{esc(sec["file"])}" class="{sec_class}" data-pltdoc="x">'
                    f'{esc(sec["title"])}</a></td></tr>'
                )
            lines.append('</table></div></div>')

        # --- On-this-page panel: section pages and leaf chapter pages only ---
        if current_chapter and (is_section_page or is_leaf_chapter):
            node = current_sec or current_chapter
            lines.append(
                f'<div class="tocviewlist">'
                '<table cellspacing="0" cellpadding="0"><tr>'
                f'<td style="width: 1em;"><a href="javascript:void(0);" title="Expand/Collapse" '
                f'class="tocviewtoggle" onclick="TocviewToggle(this,&quot;tocview_{toc_id}&quot;);">&#9658;</a></td>'
                f'<td>{esc(node["number"])}&nbsp;</td>'
                f'<td><a href="{esc(current_file)}" class="tocviewselflink" data-pltdoc="x">'
                f'{esc(node["title"])}</a></td>'
                '</tr></table>'
                f'<div class="tocviewsublistbottom" style="display: none;" id="tocview_{toc_id}">'
                '</div></div>'
            )

    lines.append('</div>')  # close tocview

    # --- "On this page" sub-TOC panel (tocsub) — only on section/leaf chapter pages.
    # The original Scribble output omits this panel on booklet and chapter-with-sections
    # pages, where it would be empty/useless.
    show_tocsub = current_booklet and current_chapter and (
        (current_sec is not None) or
        (not has_sections and current_chapter['file'] == current_file)
    )
    if show_tocsub:
        lines.append('<div class="tocsub"><div class="tocsubtitle">On this page:</div>'
                     '<table class="tocsublist" cellspacing="0"></table></div>')

    lines.append('</div>')  # close tocset
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Pandoc invocation
# ---------------------------------------------------------------------------

def pandoc_args(md_path, out_path, tocset_html, nav):
    """Build the pandoc command for a single file."""
    cmd = [
        PANDOC,
        md_path,
        '--from', 'markdown+fenced_divs+raw_html+tex_math_single_backslash'
                  '+bracketed_spans+inline_code_attributes+smart',
        '--to', 'html5',
        '--template', os.path.join(TMPL_DIR, 'dcic.html'),
        '--lua-filter', os.path.join(FILT_DIR, 'dcic-transforms.lua'),
        '--mathjax',
        '--no-highlight',
        '--variable', f'tocset_html={tocset_html}',
        '--output', out_path,
    ]
    if nav.get('prev'):
        cmd += ['--variable', f'prev={nav["prev"]}']
    if nav.get('up'):
        cmd += ['--variable', f'up={nav["up"]}']
    if nav.get('next'):
        cmd += ['--variable', f'next={nav["next"]}']
    return cmd

def run_pandoc(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print('PANDOC ERROR:', result.stderr[:500])
        return False
    return True


# ---------------------------------------------------------------------------
# Asset copying
# ---------------------------------------------------------------------------

def copy_assets(src_dir, out_dir):
    """Copy all files from src_dir to out_dir (skipping subdirectories)."""
    os.makedirs(out_dir, exist_ok=True)
    count = 0
    for name in os.listdir(src_dir):
        src = os.path.join(src_dir, name)
        if not os.path.isfile(src):
            continue
        dst = os.path.join(out_dir, name)
        if not os.path.exists(dst) or os.path.getmtime(src) > os.path.getmtime(dst):
            shutil.copy2(src, dst)
            count += 1
    if count:
        print(f'  Copied {count} static assets')


# ---------------------------------------------------------------------------
# Main build routine
# ---------------------------------------------------------------------------

def build_file(md_path, book, flat, nav_index, out_dir):
    basename_md  = os.path.basename(md_path)
    basename_html = os.path.splitext(basename_md)[0] + '.html'
    out_path     = os.path.join(out_dir, basename_html)
    nav          = nav_index.get(basename_html, {})
    tocset_html  = build_tocset_html(basename_html, book, flat, nav_index)

    import tempfile

    # Write tocset as a standalone HTML file for --include-before-body
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False,
                                     encoding='utf-8') as tf:
        tf.write(tocset_html + '\n')
        toc_tmp = tf.name

    # Pass nav metadata via YAML file
    meta = {}
    if nav.get('prev'):  meta['prev'] = nav['prev']
    if nav.get('up'):    meta['up']   = nav['up']
    if nav.get('next'):  meta['next'] = nav['next']

    with tempfile.NamedTemporaryFile('w', suffix='.yaml', delete=False,
                                     encoding='utf-8') as mf:
        yaml.dump(meta, mf, default_flow_style=False, allow_unicode=True)
        meta_tmp = mf.name

    final_cmd = PANDOC + [
        md_path,
        '--from', 'markdown+fenced_divs+raw_html+tex_math_single_backslash'
                  '+bracketed_spans+inline_code_attributes+smart',
        '--to', 'html5',
        '--template', os.path.join(TMPL_DIR, 'dcic.html'),
        '--lua-filter', os.path.join(FILT_DIR, 'dcic-transforms.lua'),
        '--mathjax',
        '--no-highlight',
        '--include-before-body', toc_tmp,
        '--metadata-file', meta_tmp,
        '--output', out_path,
    ]

    ok = run_pandoc(final_cmd)
    os.unlink(meta_tmp)
    os.unlink(toc_tmp)

    status = 'OK' if ok else 'FAIL'
    print(f'  [{status}] {basename_md} → {basename_html}')
    return ok


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Build a single .md file')
    parser.add_argument('--all', action='store_true', help='Build all chapters')
    parser.add_argument('--clean', action='store_true', help='Remove build/ first')
    parser.add_argument('--src', default=SRC_DIR, help='Source .md directory')
    parser.add_argument('--out', default=OUT_DIR, help='Output HTML directory')
    args = parser.parse_args()

    src_dir = args.src
    out_dir = args.out

    if args.clean and os.path.exists(out_dir):
        shutil.rmtree(out_dir)
        print(f'Cleaned {out_dir}')

    os.makedirs(out_dir, exist_ok=True)

    book      = load_book()
    flat      = flat_file_list(book)
    nav_index = make_nav_index(flat)

    # Copy static assets
    print('Copying assets...')
    copy_assets(ORIG_DIR, out_dir)
    # Copy root splash page assets (css/ subdir, splash image, favicon)
    splash_files = ['index.html', 'DCIC_splash.png', 'favicon.png']
    for name in splash_files:
        src = os.path.join(ROOT, name)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(out_dir, name))
    css_src = os.path.join(ROOT, 'css')
    if os.path.isdir(css_src):
        shutil.copytree(css_src, os.path.join(out_dir, 'css'), dirs_exist_ok=True)

    if args.file:
        f = args.file
        if not os.path.isabs(f):
            # Try CWD-relative first, then src_dir-relative
            if os.path.exists(f):
                f = os.path.abspath(f)
            else:
                f = os.path.join(src_dir, os.path.basename(f))
        md_files = [f]
    else:
        md_files = sorted(
            os.path.join(src_dir, f)
            for f in os.listdir(src_dir)
            if f.endswith('.md')
        )

    print(f'Building {len(md_files)} file(s)...')
    ok_count = fail_count = 0
    for md_path in md_files:
        if not os.path.exists(md_path):
            print(f'  [SKIP] {md_path} not found')
            continue
        ok = build_file(md_path, book, flat, nav_index, out_dir)
        if ok:
            ok_count += 1
        else:
            fail_count += 1

    print(f'\nDone: {ok_count} OK, {fail_count} failed.')
    if fail_count:
        sys.exit(1)


if __name__ == '__main__':
    main()
