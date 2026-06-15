#!/usr/bin/env python3
"""
convert.py  –  Convert DCIC Scribble-generated HTML to Pandoc Markdown.

Usage:
    python3 convert.py <input.html> [output.md]

If output.md is omitted, the result is written to src/<basename>.md.
"""

import sys, re, os, textwrap
sys.path.insert(0, '/tmp/pylibs')
from bs4 import BeautifulSoup, NavigableString, Tag

SRC_DIR   = os.path.join(os.path.dirname(__file__), '2025-08-27')
OUT_DIR   = os.path.join(os.path.dirname(__file__), 'src')

# ---------------------------------------------------------------------------
# Configuration tables
# ---------------------------------------------------------------------------

# Tags/classes that are raw-HTML islands — too complex to markdownify
RAW_HTML_CLASSES = frozenset([
    'HeapPart', 'HeapCode', 'EnvPart', 'ExprPart', 'HeapExpr',
    'TwoColumn', 'TwoColumnAsRows',
    'RktBlk', 'SCodeFlow', 'SVerbatim',
])

# blockquote classes → (fenced-div class, header text to drop from source)
BLOCK_CLASSES = {
    'Incercise': 'do-now',
    'Exercise':  'exercise',
    'RespCS':    'responsible-cs',
    'Strategy':  'strategy',
    'Note':      'note',
    'VSCode':    'vscode-note',
    'WorldDef':  'world-def',
}

# heading tags we recognise
HEADING_TAGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6'}

# Heading tag → markdown #-level
HTAG_LEVEL = {'h1': 1, 'h2': 2, 'h3': 3, 'h4': 4, 'h5': 5, 'h6': 6}

# Inline spans whose content we simply pass through (drop the wrapper)
TRANSPARENT_SPAN_CLASSES = frozenset([
    'SIntrapara', 'nobreak', 'mywbr', 'SAuthorListBox', 'SAuthorList',
])

# Inline spans to drop entirely (including their content)
DROP_SPAN_CLASSES = frozenset([
    'button-group', 'hspace', 'versionbox',
    'tocsublinknumber', 'toclink', 'mywbr',
])

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_classes(tag):
    return set(tag.get('class') or [])

def has_class(tag, *cls):
    return bool(get_classes(tag) & set(cls))

def is_raw_html(tag):
    return isinstance(tag, Tag) and bool(get_classes(tag) & RAW_HTML_CLASSES)

def node_text(node):
    """Get all text from a node, collapsing whitespace."""
    return re.sub(r'\s+', ' ', node.get_text()).strip()

def escape_md(text):
    """Escape characters that have special meaning in Markdown prose."""
    # Only escape where it matters at the start of a line or in flowing text.
    # We do NOT escape inside code spans / code blocks.
    text = text.replace('\\', '\\\\')
    # Escape leading # so they don't become headings
    text = re.sub(r'^(#+)', r'\\\1', text, flags=re.MULTILINE)
    return text

def code_lang(tag):
    """Extract language label from a sourceCode/sourceCodeWrapper element."""
    lang = tag.get('data-lang') or ''
    # normalise python variants
    if 'python' in lang or lang == 'text/x-python':
        return 'python'
    if lang == 'pyret':
        return 'pyret'
    if lang:
        return lang
    # look for a sourceLangLabel sibling/child
    wrapper = tag.find_parent(class_='sourceCodeWrapper') or tag
    label = wrapper.find(class_='sourceLangLabel')
    if label:
        lab = label.get('data-label', '').lower()
        if 'python' in lab:
            return 'python'
        if 'pyret' in lab:
            return 'pyret'
    return ''

def extract_code_text(tag):
    """Extract raw code text from a sourceCode pre/code element."""
    code = tag.find('code') if tag.name != 'code' else tag
    pre  = tag.find('pre')  if tag.name != 'pre'  else tag
    target = code or pre or tag
    return target.get_text()

def strip_section_number(text):
    """Remove leading section numbers like '3.1.2 ' or 'I ' from heading text."""
    return re.sub(r'^[\d\.]+\s+', '', re.sub(r'^[IVXLC]+\s+', '', text.strip()))

def normalize_anchor(raw):
    """Convert Scribble anchor like '(part._getting-started)' → 'getting-started'."""
    m = re.search(r'part\._([^)]+)', raw or '')
    if m:
        slug = m.group(1)
        slug = slug.replace('~3a', '-').replace('~7e', '-')
        slug = re.sub(r'[^a-zA-Z0-9-]', '-', slug)
        slug = re.sub(r'-+', '-', slug).strip('-')
        return slug
    return re.sub(r'[^a-zA-Z0-9-]', '-', (raw or '').strip('()')).strip('-')

# ---------------------------------------------------------------------------
# Front-matter extraction
# ---------------------------------------------------------------------------

def extract_front_matter(soup, filename):
    """Return a dict of YAML front matter fields."""
    fm = {'source_file': filename}

    title_tag = soup.find('title')
    if title_tag:
        raw_title = title_tag.get_text()
        # Strip section number: "3.1 Getting Started" → "Getting Started"
        fm['title'] = strip_section_number(raw_title)
        # Keep section number separately
        m = re.match(r'^([\d\.]+|[IVXLC]+)\s+', raw_title.strip())
        if m:
            fm['section_number'] = m.group(1)

    # Navigation links
    nav = soup.find('div', class_='navsettop')
    if nav:
        for a in nav.find_all('a', href=True):
            href = a['href']
            if not href or href.startswith('javascript'):
                continue
            rel = a.get('rel')
            if rel:
                key = rel[0] if isinstance(rel, list) else rel
                fm[key] = href
            else:
                # "up" link has no rel attribute — detect by link text
                text = a.get_text(strip=True)
                if text == 'up':
                    fm['up'] = href

    return fm

def front_matter_str(fm):
    lines = ['---']
    for key in ('title', 'section_number', 'source_file', 'prev', 'up', 'next'):
        if key in fm:
            val = fm[key]
            if any(c in str(val) for c in ':#{}[]'):
                lines.append(f'{key}: "{val}"')
            else:
                lines.append(f'{key}: {val}')
    lines.append('---')
    return '\n'.join(lines)

# ---------------------------------------------------------------------------
# Core recursive converter
# ---------------------------------------------------------------------------

class Converter:
    def __init__(self):
        self._raw_html_counter = 0

    def convert(self, node):
        """Dispatch on node type; return a Markdown string."""
        if isinstance(node, NavigableString):
            return self._text(node)
        if not isinstance(node, Tag):
            return ''
        return self._tag(node)

    # -- text ----------------------------------------------------------------

    def _text(self, node):
        text = str(node)
        # Collapse runs of whitespace to single space, keep newlines minimal
        text = re.sub(r'[ \t]+', ' ', text)
        return text

    # -- tag dispatch --------------------------------------------------------

    def _tag(self, tag):
        cls = get_classes(tag)

        # Things to drop entirely
        if cls & DROP_SPAN_CLASSES:
            return ''
        if has_class(tag, 'versionbox'):
            return ''
        # Navigation / TOC scaffolding
        if cls & {'tocset', 'navsettop', 'navsetbottom',
                   'navsettop navset', 'navsetbottom navset'}:
            return ''
        if tag.name in ('script', 'style'):
            return ''

        # Raw HTML islands
        if cls & RAW_HTML_CLASSES:
            return self._raw_html(tag)

        # Headings
        if tag.name in HEADING_TAGS and 'heading' in cls:
            return self._heading(tag)

        # Sections
        if tag.name == 'section':
            return self._section(tag)

        # Paragraphs
        if tag.name == 'p':
            return self._paragraph(tag)

        # Block code (sourceCodeWrapper)
        if 'sourceCodeWrapper' in cls:
            return self._code_block(tag)

        # Custom semantic blocks (Incercise, Exercise, …)
        for bclass, div_class in BLOCK_CLASSES.items():
            if bclass in cls:
                return self._custom_block(tag, div_class)

        # REPL interaction
        if 'PyretReplInteraction' in cls:
            return self._repl(tag)

        # Images
        if tag.name == 'img':
            return self._image(tag)

        # Lists
        if tag.name in ('ul', 'ol'):
            return self._list(tag)
        if tag.name == 'li':
            return self._list_item(tag)

        # Blockquote (generic – not a custom block)
        if tag.name == 'blockquote' and not (cls & set(BLOCK_CLASSES)):
            return self._children_block(tag)

        # Tables (non-REPL, non-custom) — keep as raw HTML
        if tag.name == 'table' and 'PyretReplInteraction' not in cls \
                and 'TwoColumn' not in cls and 'TwoColumnAsRows' not in cls:
            # Could be a sub-TOC table right after a heading — skip those
            if self._is_toc_table(tag):
                return ''
            return self._raw_html(tag)

        # Div / span containers — transparent or special
        if tag.name in ('div', 'span', 'section'):
            return self._container(tag)

        # Inline elements
        if tag.name in ('em', 'i') or 'emph' in cls:
            inner = self._inline_children(tag)
            return f'*{inner}*' if inner.strip() else ''

        if tag.name in ('strong', 'b'):
            inner = self._inline_children(tag)
            return f'**{inner}**' if inner.strip() else ''

        if tag.name == 'code' or 'sourceCode' in cls:
            return self._inline_code(tag)

        if tag.name == 'a':
            return self._link(tag)

        if tag.name == 'wbr':
            return ''

        if tag.name in ('br',):
            return '\n'

        # Margin notes
        if 'refelem' in cls:
            return self._margin_note(tag)

        # Smaller spans → {.smaller}
        if 'Smaller' in cls:
            inner = self._inline_children(tag)
            return f'[{inner}]{{.smaller}}' if inner.strip() else ''

        # stt (monospace inline not already a code tag)
        if 'stt' in cls:
            inner = self._inline_children(tag)
            inner = inner.strip()
            if inner:
                return f'`{inner}`'
            return ''

        # SCentered
        if 'SCentered' in cls:
            return self._fenced_div(tag, 'centered')

        # Fall back: recurse into children
        return self._children_block(tag)

    # -- headings ------------------------------------------------------------

    def _heading(self, tag):
        level = HTAG_LEVEL.get(tag.name, 3)
        # Find anchor name
        anchor_tag = tag.find('a', attrs={'name': True})
        anchor = normalize_anchor(anchor_tag['name']) if anchor_tag else ''
        # Strip span.button-group, span.stt, a[name], a.heading-anchor
        for el in tag.find_all(class_=['button-group', 'stt']):
            el.decompose()
        for el in tag.find_all('a'):
            el.decompose()
        raw_text = re.sub(r'\s+', ' ', tag.get_text(' ', strip=True)).strip()
        title = strip_section_number(raw_text)
        hashes = '#' * level
        anchor_attr = f' {{#{anchor}}}' if anchor else ''
        return f'\n{hashes} {title}{anchor_attr}\n'

    # -- sections ------------------------------------------------------------

    def _section(self, tag):
        parts = []
        for child in tag.children:
            if isinstance(child, NavigableString):
                t = str(child).strip()
                if t:
                    parts.append(t)
                continue
            cls = get_classes(child)
            # Skip the mini sub-TOC table that appears right after a heading
            if child.name == 'table' and self._is_toc_table(child):
                continue
            result = self.convert(child)
            if result.strip():
                parts.append(result)
        return '\n\n'.join(p.strip() for p in parts if p.strip())

    def _is_toc_table(self, tag):
        """Return True if this table is a Scribble mini-TOC (links to sub-sections)."""
        if tag.name != 'table':
            return False
        links = tag.find_all('a', class_='toclink')
        return len(links) > 0

    # -- paragraphs ----------------------------------------------------------

    def _paragraph(self, tag):
        content = self._inline_children(tag)
        content = content.strip()
        if not content:
            return ''
        return content

    # -- inline children -----------------------------------------------------

    def _inline_children(self, tag):
        parts = []
        for child in tag.children:
            if isinstance(child, NavigableString):
                parts.append(self._text(child))
            else:
                cls = get_classes(child)
                # sourceCodeWrapper inside a paragraph = inline code block context
                if 'sourceCodeWrapper' in cls:
                    parts.append(self._code_block(child))
                elif 'PyretReplInteraction' in cls:
                    parts.append(self._repl(child))
                elif child.name == 'img':
                    parts.append(self._image(child))
                elif cls & RAW_HTML_CLASSES:
                    parts.append(self._raw_html(child))
                elif child.name in ('ul', 'ol'):
                    parts.append('\n\n' + self._list(child) + '\n\n')
                elif child.name == 'blockquote':
                    parts.append('\n\n' + self._tag(child) + '\n\n')
                elif 'SIntrapara' in cls or 'nobreak' in cls:
                    parts.append(self._inline_children(child))
                elif 'refelem' in cls:
                    parts.append(self._margin_note(child))
                elif child.name == 'p':
                    # Recurse without stripping so trailing \n from inner
                    # code blocks isn't lost before adjacent inline text.
                    parts.append(self._inline_children(child))
                else:
                    parts.append(self._tag(child))
        return ''.join(parts)

    # -- block children (sequence of block elements) -------------------------

    def _children_block(self, tag):
        parts = []
        for child in tag.children:
            if isinstance(child, NavigableString):
                t = str(child).strip()
                if t:
                    parts.append(t)
            else:
                result = self.convert(child)
                if result.strip():
                    parts.append(result.strip())
        return '\n\n'.join(parts)

    # -- code blocks ---------------------------------------------------------

    def _code_block(self, tag):
        lang = ''
        code_text = ''

        wrapper = tag if 'sourceCodeWrapper' in get_classes(tag) else \
                  tag.find_parent(class_='sourceCodeWrapper') or tag

        pre = wrapper.find('pre') if wrapper else tag.find('pre')
        if pre:
            lang = code_lang(pre)
            code = pre.find('code')
            code_text = (code or pre).get_text()
        else:
            code = tag.find('code')
            if code:
                lang = code_lang(code)
                code_text = code.get_text()
            else:
                code_text = tag.get_text()

        # Strip trailing newline added by Scribble
        code_text = code_text.rstrip('\n')
        fence = '```'
        return f'\n{fence}{lang}\n{code_text}\n{fence}\n'

    # -- inline code ---------------------------------------------------------

    def _inline_code(self, tag):
        # Find the actual code text
        if tag.name == 'code':
            text = tag.get_text()
        else:
            code = tag.find('code')
            text = (code or tag).get_text()
        if not text.strip():
            return ''
        lang = code_lang(tag)
        if lang:
            return f'`{text}`{{.{lang}}}'
        return f'`{text}`'

    # -- REPL interactions ---------------------------------------------------

    def _repl(self, tag):
        """Convert a PyretReplInteraction table to a fenced div."""
        # Detect type: input-only vs input+output
        rows = tag.find_all('tr', recursive=False)
        if not rows:
            return self._raw_html(tag)

        first_td = rows[0].find('td')
        if not first_td:
            return self._raw_html(tag)

        # Check for nested PyretReplInteraction (input+output pattern)
        nested = first_td.find('table', class_='PyretReplInteraction')

        if nested and len(rows) == 2:
            # input + output
            input_pre = nested.find('pre')
            input_code = (input_pre.find('code') or input_pre).get_text() if input_pre else ''
            input_lang = code_lang(input_pre) if input_pre else 'pyret'

            output_td = rows[1].find('td')
            output_pre = output_td.find('pre') if output_td else None
            output_code = (output_pre.find('code') or output_pre).get_text() if output_pre else ''
            output_lang = code_lang(output_pre) if output_pre else input_lang

            return (
                f'\n::: {{.pyret-repl}}\n'
                f'``` {input_lang}\n{input_code.rstrip()}\n```\n'
                f'``` output\n{output_code.rstrip()}\n```\n'
                f':::\n'
            )
        else:
            # input-only (prompt shown, no output yet)
            bq = first_td.find('blockquote', class_='PyretRepl')
            pre = bq.find('pre') if bq else first_td.find('pre')
            if not pre:
                # Just a nested outer table shown without output
                if nested:
                    return self._repl(nested)
                return self._raw_html(tag)
            input_code = (pre.find('code') or pre).get_text()
            input_lang = code_lang(pre) or 'pyret'
            return (
                f'\n::: {{.pyret-repl}}\n'
                f'``` {input_lang}\n{input_code.rstrip()}\n```\n'
                f':::\n'
            )

    # -- custom blocks -------------------------------------------------------

    def _custom_block(self, tag, div_class):
        # Strip the header paragraph (IncerciseHeader, ExerciseHeader, etc.)
        body_bq = tag.find('blockquote', class_=lambda c: c and c[0].endswith('Body'))
        if body_bq:
            content = self._children_block(body_bq)
        else:
            # Fallback: skip the first <p> (which is always the header label)
            children = [c for c in tag.children
                        if not (isinstance(c, NavigableString) and not c.strip())]
            if children and isinstance(children[0], Tag) and \
               any(x.endswith('Header') for x in get_classes(children[0])):
                children = children[1:]
            parts = []
            for child in children:
                r = self.convert(child)
                if r.strip():
                    parts.append(r.strip())
            content = '\n\n'.join(parts)

        content = content.strip()
        return f'\n::: {{.{div_class}}}\n{content}\n:::\n'

    def _fenced_div(self, tag, div_class):
        content = self._children_block(tag).strip()
        return f'\n::: {{.{div_class}}}\n{content}\n:::\n'

    # -- margin notes --------------------------------------------------------

    def _margin_note(self, tag):
        refcontent = tag.find(class_='refcontent')
        if not refcontent:
            return ''
        inner = self._inline_children(refcontent).strip()
        if not inner:
            return ''
        # Use a span with class margin-note
        return f'[{inner}]{{.margin-note}}'

    # -- images --------------------------------------------------------------

    def _image(self, tag):
        src = tag.get('src', '')
        alt = tag.get('alt', '')
        width  = tag.get('width', '')
        height = tag.get('height', '')
        attrs = ''
        if width or height:
            parts = []
            if width:  parts.append(f'width="{width}"')
            if height: parts.append(f'height="{height}"')
            attrs = '{' + ' '.join(parts) + '}'
        return f'![{alt}]({src}){attrs}'

    # -- links ---------------------------------------------------------------

    def _link(self, tag):
        href = tag.get('href', '')
        if not href or href.startswith('javascript:'):
            return self._inline_children(tag)
        # Convert Scribble anchor URLs to clean ones
        href = re.sub(r'%28part\._([^%]+)%29',
                      lambda m: '#' + normalize_anchor('(part._' + m.group(1) + ')'),
                      href)
        text = self._inline_children(tag).strip()
        if not text:
            return ''
        return f'[{text}]({href})'

    # -- lists ---------------------------------------------------------------

    def _list(self, tag):
        items = []
        for li in tag.find_all('li', recursive=False):
            item = self._list_item(li)
            items.append(item)
        if tag.name == 'ol':
            return '\n'.join(f'{i+1}. {item}' for i, item in enumerate(items))
        return '\n'.join(f'- {item}' for item in items)

    def _list_item(self, li):
        parts = []
        for child in li.children:
            if isinstance(child, NavigableString):
                t = str(child).strip()
                if t:
                    parts.append(t)
            else:
                r = self.convert(child)
                if r.strip():
                    parts.append(r.strip())
        content = '\n\n'.join(parts)
        # Indent continuation lines for nested blocks
        lines = content.split('\n')
        if len(lines) > 1:
            content = lines[0] + '\n' + '\n'.join('  ' + l for l in lines[1:])
        return content

    # -- container (div / span passthrough) ----------------------------------

    def _container(self, tag):
        cls = get_classes(tag)

        if cls & TRANSPARENT_SPAN_CLASSES:
            return self._children_block(tag)

        if cls & DROP_SPAN_CLASSES:
            return ''

        # HeapExpr, heapref etc. that sneak through
        if cls & RAW_HTML_CLASSES:
            return self._raw_html(tag)

        # SIntrapara — flatten
        if 'SIntrapara' in cls:
            return self._children_block(tag)

        # Generic passthrough
        return self._children_block(tag)

    # -- raw HTML passthrough ------------------------------------------------

    def _raw_html(self, tag):
        html = str(tag)
        return f'\n```{{=html}}\n{html}\n```\n'


# ---------------------------------------------------------------------------
# Top-level file conversion
# ---------------------------------------------------------------------------

def convert_file(html_path, md_path=None):
    basename = os.path.basename(html_path)
    if md_path is None:
        stem = os.path.splitext(basename)[0]
        md_path = os.path.join(OUT_DIR, stem + '.md')

    with open(html_path, encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    fm = extract_front_matter(soup, basename)

    # Find the main content div
    main = soup.find('div', class_='main')
    if not main:
        main = soup.find('body') or soup

    # Remove navigation scaffolding in-place
    for el in main.find_all(class_=['navsettop', 'navsetbottom',
                                     'tocsettoggle', 'nosearchform']):
        el.decompose()

    converter = Converter()
    body = converter.convert(main)

    # Clean up excessive blank lines
    body = re.sub(r'\n{4,}', '\n\n\n', body)
    body = body.strip()

    output = front_matter_str(fm) + '\n\n' + body + '\n'

    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f'  {basename} → {os.path.relpath(md_path)}')
    return md_path


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    html_path = sys.argv[1]
    md_path   = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.isabs(html_path):
        # Try relative to SRC_DIR first
        candidate = os.path.join(SRC_DIR, html_path)
        if os.path.exists(candidate):
            html_path = candidate

    convert_file(html_path, md_path)
