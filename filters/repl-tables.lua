-- repl-tables.lua
-- Converts .pyret-repl fenced divs back to PyretReplInteraction HTML tables.
--
-- Markdown source format:
--
--   ::: {.pyret-repl}
--   ``` pyret
--   3 + 5
--   ```
--   ``` output
--   8
--   ```
--   :::
--
-- A block with only the first code block (no "output" block) becomes an
-- input-only interaction (the prompt is shown, no result yet).
--
-- The reconstructed HTML matches the Scribble output exactly:
--
--   Input-only:
--     <table class="PyretReplInteraction">
--       <tr><td><blockquote class="PyretRepl">
--         <p class="PyretReplPrompt"></p>
--         <p><div class="sourceCodeWrapper">...<pre data-lang="pyret"><code>INPUT</code></pre>...</div></p>
--       </blockquote></td></tr>
--     </table>
--
--   Input + output:
--     <table class="PyretReplInteraction">
--       <tr><td>
--         <table class="PyretReplInteraction">   ← nested
--           <tr><td><blockquote class="PyretRepl">...INPUT...</blockquote></td></tr>
--         </table>
--       </td></tr>
--       <tr><td><p><div class="sourceCodeWrapper">...OUTPUT...</div></p></td></tr>
--     </table>

local function lang_label(lang)
  if lang == "python" or lang == "text/x-python" then
    return "Python"
  elseif lang == "pyret" then
    return "Pyret"
  elseif lang == "output" then
    return ""
  else
    return lang or "Pyret"
  end
end

local function code_wrapper(code, lang)
  -- Reconstruct the sourceCodeWrapper div + pre/code structure
  local label = lang_label(lang)
  local data_lang = (lang == "output") and "pyret" or (lang or "pyret")
  local label_span = label ~= ""
    and '<span class="sourceLangLabel" data-label="' .. label .. '"></span>'
    or  ""
  return
    '<div class="sourceCodeWrapper">'
    .. label_span
    .. '<div class="sourceCode">'
    .. '<pre class="sourceCode" data-lang="' .. data_lang .. '">'
    .. '<code class="sourceCode" data-lang="' .. data_lang .. '">'
    .. code
    .. '</code></pre>'
    .. '</div>'
    .. '</div>'
end

local function repl_input_table(code, lang)
  return
    '<table cellpadding="0" cellspacing="0" class="PyretReplInteraction">'
    .. '<tr><td>'
    .. '<blockquote class="PyretRepl">'
    .. '<p class="PyretReplPrompt"></p>'
    .. '<p>' .. code_wrapper(code, lang) .. '</p>'
    .. '</blockquote>'
    .. '</td></tr>'
    .. '</table>'
end

local function div_has_class(div, cls)
  for _, c in ipairs(div.classes) do
    if c == cls then return true end
  end
  return false
end

function Div(div)
  if not div_has_class(div, "pyret-repl") then return nil end

  -- Collect code blocks inside the div
  local blocks = {}
  for _, blk in ipairs(div.content) do
    if blk.t == "CodeBlock" then
      local lang = blk.attr.classes[1] or "pyret"
      table.insert(blocks, { lang = lang, code = blk.text })
    end
  end

  if #blocks == 0 then return nil end

  local input_block  = blocks[1]
  local output_block = blocks[2]  -- may be nil

  if output_block then
    -- Input + output interaction
    local outer_html =
      '<table cellpadding="0" cellspacing="0" class="PyretReplInteraction">'
      .. '<tr><td>'
      .. repl_input_table(input_block.code, input_block.lang)
      .. '</td></tr>'
      .. '<tr><td>'
      .. '<p>' .. code_wrapper(output_block.code, output_block.lang) .. '</p>'
      .. '</td></tr>'
      .. '</table>'
    return pandoc.RawBlock("html", outer_html)
  else
    -- Input-only interaction
    return pandoc.RawBlock("html", repl_input_table(input_block.code, input_block.lang))
  end
end
