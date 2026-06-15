-- custom-blocks.lua
-- Converts Pandoc fenced divs back to DCIC/Scribble-style HTML blockquotes.
--
-- Mapping (Markdown fenced div class → HTML blockquote class):
--   do-now          → Incercise   / IncerciseHeader "Do Now!"
--   exercise        → Exercise    / ExerciseHeader  "Exercise"
--   responsible-cs  → RespCS      / RespCSHeader    "Responsible Computing"
--   strategy        → Strategy    / StrategyHeader  "Strategy"
--   note            → Note        (no explicit header element)
--   vscode-note     → VSCode      (no explicit header element)
--   world-def       → WorldDef    (no explicit header element)
--   centered        → SCentered   (div, not blockquote)

local block_map = {
  ["do-now"]         = { class = "Incercise", header = "Do Now!",              body_class = "IncerciseBody" },
  ["exercise"]       = { class = "Exercise",  header = "Exercise",             body_class = "ExerciseBody"  },
  ["responsible-cs"] = { class = "RespCS",    header = "Responsible Computing",body_class = "RespCSBody"    },
  ["strategy"]       = { class = "Strategy",  header = "Strategy",             body_class = "StrategyBody"  },
  ["note"]           = { class = "Note",      header = nil,                    body_class = nil             },
  ["vscode-note"]    = { class = "VSCode",    header = nil,                    body_class = nil             },
  ["world-def"]      = { class = "WorldDef",  header = nil,                    body_class = nil             },
}

local function div_has_class(div, cls)
  for _, c in ipairs(div.classes) do
    if c == cls then return true end
  end
  return false
end

local function render_body(blocks)
  -- Render the inner blocks as a Pandoc RawBlock of HTML.
  -- We use pandoc.write to turn the inner blocks back to HTML.
  local doc = pandoc.Pandoc(blocks)
  return pandoc.write(doc, 'html')
end

function Div(div)
  -- SCentered
  if div_has_class(div, "centered") then
    local inner_html = render_body(div.content)
    return pandoc.RawBlock("html",
      '<div class="SCentered">' .. inner_html .. '</div>')
  end

  for md_class, info in pairs(block_map) do
    if div_has_class(div, md_class) then
      local inner_html = render_body(div.content)

      if info.header then
        -- With explicit header + body sub-blockquote
        return pandoc.RawBlock("html",
          '<blockquote class="' .. info.class .. '">'
          .. '<p class="' .. info.class .. 'Header">' .. info.header .. '</p>'
          .. '<blockquote class="' .. info.body_class .. '">'
          .. inner_html
          .. '</blockquote>'
          .. '</blockquote>')
      else
        -- Header-less block
        return pandoc.RawBlock("html",
          '<blockquote class="' .. info.class .. '">'
          .. inner_html
          .. '</blockquote>')
      end
    end
  end
end
