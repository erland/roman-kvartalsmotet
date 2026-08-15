-- Formatera kanoniska H1-rubriker som tvådelade PDF-kapitelstarter.
-- Stöder "# Kapitel 1 – Titel" och "# 1. Titel".
-- Viktigt: använd plain string-sökning för " – " så Lua inte delar UTF-8-byte i en pattern-klass.

local function latex_escape(value)
  value = value:gsub("\\", "\\textbackslash{}")
  value = value:gsub("([{}#$%%&_])", "\\%1")
  value = value:gsub("%^", "\\textasciicircum{}")
  value = value:gsub("~", "\\textasciitilde{}")
  return value
end

local function parse_chapter_title(text)
  local number, rest = text:match("^%s*Kapitel%s+(%d+)%s+(.+)%s*$")
  if number then
    local pos = rest:find("–", 1, true)
    if pos then
      return number, rest:sub(pos + #"–"):gsub("^%s+", ""):gsub("%s+$", "")
    end
    pos = rest:find("-", 1, true)
    if pos then
      return number, rest:sub(pos + 1):gsub("^%s+", ""):gsub("%s+$", "")
    end
  end

  number, rest = text:match("^%s*(%d+)%.%s+(.+)%s*$")
  if number then
    return number, rest:gsub("^%s+", ""):gsub("%s+$", "")
  end

  return nil, nil
end

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)
  local number, title = parse_chapter_title(text)
  if not number then
    return nil
  end

  return pandoc.RawBlock(
    "latex",
    "\\bookchapter{" .. latex_escape(number) .. "}{" .. latex_escape(title) .. "}{" .. latex_escape(text) .. "}"
  )
end
