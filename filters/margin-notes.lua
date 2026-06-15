-- margin-notes.lua
-- Converts [content]{.margin-note} spans and {.smaller} spans back to
-- their Scribble HTML counterparts.
--
--   [text]{.margin-note}  →  <span class="refelem"><span class="refcolumn">
--                               <span class="refcontent">text</span>
--                             </span></span>
--
--   [text]{.smaller}      →  <span class="Smaller">text</span>

local function lang_label(lang)
  if lang == "python" or lang == "text/x-python" then return "Python"
  elseif lang == "pyret" then return "Pyret"
  elseif lang == "output" then return ""
  else return lang or "" end
end

local function span_has_class(span, cls)
  for _, c in ipairs(span.classes) do
    if c == cls then return true end
  end
  return false
end

local function inlines_to_html(inlines)
  local doc = pandoc.Pandoc({ pandoc.Plain(inlines) })
  -- Strip the wrapping <p> tags that pandoc adds
  local html = pandoc.write(doc, 'html')
  html = html:gsub("^<p>", ""):gsub("</p>%s*$", "")
  return html
end

function Span(span)
  if span_has_class(span, "margin-note") then
    local inner = inlines_to_html(span.content)
    return pandoc.RawInline("html",
      '<span class="refelem">'
      .. '<span class="refcolumn">'
      .. '<span class="refcontent">' .. inner .. '</span>'
      .. '</span>'
      .. '</span>')
  end

  if span_has_class(span, "smaller") then
    local inner = inlines_to_html(span.content)
    return pandoc.RawInline("html",
      '<span class="Smaller">' .. inner .. '</span>')
  end
end

-- Escape HTML entities in code text
local function html_escape(s)
  s = s:gsub("&", "&amp;")
  s = s:gsub("<", "&lt;")
  s = s:gsub(">", "&gt;")
  return s
end

-- Fenced code blocks (``` pyret / ``` python) → sourceCodeWrapper HTML
-- so they get the same data-lang attributes as the originals.
function CodeBlock(block)
  local lang = block.attr.classes[1] or ""
  if lang == "" then return nil end
  local label = lang_label(lang)
  local label_span = label ~= ""
    and '<span class="sourceLangLabel" data-label="' .. label .. '"></span>'
    or  ""
  local html =
    '<div class="sourceCodeWrapper">'
    .. label_span
    .. '<div class="sourceCode">'
    .. '<pre class="sourceCode" data-lang="' .. lang .. '">'
    .. '<code class="sourceCode" data-lang="' .. lang .. '">'
    .. html_escape(block.text)
    .. '</code></pre>'
    .. '</div>'
    .. '</div>'
  return pandoc.RawBlock("html", html)
end

-- Also handle inline code with .pyret or .python class:
-- `code`{.pyret}  →  <span title="Pyret" class="sourceCode">
--                       <code class="sourceCode" data-lang="pyret">code</code>
--                     </span>
function Code(code)
  local lang = code.attr.classes[1]
  if lang == "pyret" or lang == "python" then
    local label = lang == "pyret" and "Pyret" or "Python"
    return pandoc.RawInline("html",
      '<span title="' .. label .. '" class="sourceCode">'
      .. '<code class="sourceCode" data-lang="' .. lang .. '">'
      .. pandoc.utils.stringify(pandoc.Str(code.text))
      .. '</code>'
      .. '</span>')
  end
end
