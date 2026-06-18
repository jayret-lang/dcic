-- dcic-transforms.lua
-- Single combined filter for all DCIC HTML transformations.
-- Uses topdown traversal so .pyret-repl Divs are converted to raw HTML
-- before their children are visited by the CodeBlock handler.

-- ---------------------------------------------------------------------------
-- Helpers
-- ---------------------------------------------------------------------------

local function div_has_class(el, cls)
  for _, c in ipairs(el.classes or {}) do
    if c == cls then return true end
  end
  return false
end

local function span_has_class(el, cls)
  for _, c in ipairs(el.classes or {}) do
    if c == cls then return true end
  end
  return false
end

local function html_escape(s)
  s = s:gsub("&", "&amp;")
  s = s:gsub("<", "&lt;")
  s = s:gsub(">", "&gt;")
  return s
end

local function lang_label(lang)
  if lang == "python" or lang == "text/x-python" then return "Python"
  elseif lang == "pyret" or lang == "jayret" then return "Jayret"
  elseif lang == "pyret-deferred" then return "Pyret (deferred in Jayret)"
  elseif lang == "output" then return ""
  else return lang or "" end
end

-- ---------------------------------------------------------------------------
-- Atomic HTML generators (used by both inline code filter and block rendering)
-- ---------------------------------------------------------------------------

local function code_wrapper_html(code_text, lang)
  local label     = lang_label(lang)
  local data_lang = (lang == "output") and "jayret" or (lang or "jayret")
  local label_span = label ~= ""
    and '<span class="sourceLangLabel" data-label="' .. label .. '"></span>'
    or  ""
  return
    '<div class="sourceCodeWrapper">'
    .. label_span
    .. '<div class="sourceCode">'
    .. '<pre class="sourceCode" data-lang="' .. data_lang .. '">'
    .. '<code class="sourceCode" data-lang="' .. data_lang .. '">'
    .. html_escape(code_text)
    .. '</code></pre>'
    .. '</div>'
    .. '</div>'
end

local function inline_code_html(text, lang)
  local label = lang_label(lang)
  return
    '<span title="' .. label .. '" class="sourceCode">'
    .. '<code class="sourceCode" data-lang="' .. lang .. '">'
    .. html_escape(text)
    .. '</code>'
    .. '</span>'
end

-- ---------------------------------------------------------------------------
-- Element-level transform functions (reused for pre-rendering inner blocks)
-- ---------------------------------------------------------------------------

local function transform_CodeBlock(block)
  local lang = block.attr.classes[1] or ""
  if lang == "" then return nil end
  return pandoc.RawBlock("html", code_wrapper_html(block.text, lang))
end

local function transform_Code(code)
  local lang = code.attr.classes[1]
  if lang == "pyret" or lang == "jayret" or lang == "python" then
    return pandoc.RawInline("html", inline_code_html(code.text, lang))
  end
end

local function transform_Span(span)
  if span_has_class(span, "margin-note") then
    local doc  = pandoc.Pandoc({ pandoc.Plain(span.content) })
    local html = pandoc.write(doc, "html")
    html = html:gsub("^<p>", ""):gsub("</p>%s*$", "")
    return pandoc.RawInline("html",
      '<span class="refelem">'
      .. '<span class="refcolumn">'
      .. '<span class="refcontent">' .. html .. '</span>'
      .. '</span>'
      .. '</span>')
  end
  if span_has_class(span, "smaller") then
    local doc  = pandoc.Pandoc({ pandoc.Plain(span.content) })
    local html = pandoc.write(doc, "html")
    html = html:gsub("^<p>", ""):gsub("</p>%s*$", "")
    return pandoc.RawInline("html", '<span class="Smaller">' .. html .. '</span>')
  end
end

-- ---------------------------------------------------------------------------
-- Pre-render inner blocks: apply code/inline transforms before pandoc.write()
-- This ensures custom block content has proper data-lang attributes.
-- ---------------------------------------------------------------------------

local inner_filter = {
  CodeBlock = transform_CodeBlock,
  Code      = transform_Code,
  Span      = transform_Span,
}

local function blocks_to_html(blocks)
  local doc = pandoc.Pandoc(blocks)
  doc = doc:walk(inner_filter)
  return pandoc.write(doc, "html")
end

-- ---------------------------------------------------------------------------
-- REPL interaction generator
-- ---------------------------------------------------------------------------

local function repl_input_table(code, lang)
  return
    '<table cellpadding="0" cellspacing="0" class="JayretReplInteraction">'
    .. '<tr><td>'
    .. '<blockquote class="JayretRepl">'
    .. '<p class="JayretReplPrompt"></p>'
    .. '<p>' .. code_wrapper_html(code, lang) .. '</p>'
    .. '</blockquote>'
    .. '</td></tr>'
    .. '</table>'
end

local function handle_repl(div)
  local blocks = {}
  for _, blk in ipairs(div.content) do
    if blk.t == "CodeBlock" then
      local lang = blk.attr.classes[1] or "jayret"
      table.insert(blocks, { lang = lang, code = blk.text })
    end
  end
  if #blocks == 0 then return nil end

  local inp = blocks[1]
  local out = blocks[2]

  if out then
    return pandoc.RawBlock("html",
      '<table cellpadding="0" cellspacing="0" class="JayretReplInteraction">'
      .. '<tr><td>' .. repl_input_table(inp.code, inp.lang) .. '</td></tr>'
      .. '<tr><td><p>' .. code_wrapper_html(out.code, out.lang) .. '</p></td></tr>'
      .. '</table>')
  else
    return pandoc.RawBlock("html", repl_input_table(inp.code, inp.lang))
  end
end

-- ---------------------------------------------------------------------------
-- Custom block map
-- ---------------------------------------------------------------------------

local block_map = {
  ["do-now"]         = { class = "Incercise", header = "Do Now!",               body_class = "IncerciseBody" },
  ["exercise"]       = { class = "Exercise",  header = "Exercise",              body_class = "ExerciseBody"  },
  ["responsible-cs"] = { class = "RespCS",    header = "Responsible Computing", body_class = "RespCSBody"    },
  ["strategy"]       = { class = "Strategy",  header = "Strategy",              body_class = "StrategyBody"  },
  ["note"]           = { class = "Note",      header = nil,                     body_class = nil             },
  ["vscode-note"]    = { class = "VSCode",    header = nil,                     body_class = nil             },
  ["world-def"]      = { class = "WorldDef",  header = nil,                     body_class = nil             },
}

local function handle_custom_block(div, info)
  local inner_html = blocks_to_html(div.content)  -- applies inner_filter first
  if info.header then
    return pandoc.RawBlock("html",
      '<blockquote class="' .. info.class .. '">'
      .. '<p class="' .. info.class .. 'Header">' .. info.header .. '</p>'
      .. '<blockquote class="' .. info.body_class .. '">'
      .. inner_html
      .. '</blockquote>'
      .. '</blockquote>')
  else
    return pandoc.RawBlock("html",
      '<blockquote class="' .. info.class .. '">'
      .. inner_html
      .. '</blockquote>')
  end
end

-- ---------------------------------------------------------------------------
-- Filter passes
-- ---------------------------------------------------------------------------

-- Pass 1 (topdown): claim Divs that own their children.
-- Returning a value stops Pandoc from recursing into children.
local pass1 = {
  traverse = "topdown",

  Div = function(div)
    if div_has_class(div, "pyret-repl") then
      return handle_repl(div)
    end
    for md_class, info in pairs(block_map) do
      if div_has_class(div, md_class) then
        return handle_custom_block(div, info)
      end
    end
    if div_has_class(div, "centered") then
      local inner_html = blocks_to_html(div.content)
      return pandoc.RawBlock("html", '<div class="SCentered">' .. inner_html .. '</div>')
    end
    return nil  -- recurse normally
  end,
}

-- Pass 2: remaining standalone elements (not inside already-converted blocks)
local pass2 = {
  CodeBlock = transform_CodeBlock,
  Code      = transform_Code,
  Span      = transform_Span,
}

return { pass1, pass2 }
