-- Formatera kanoniska H1-rubriker som tvådelade PDF-kapitelstarter.
-- Stöder "# Kapitel 1 – Titel" och "# 1. Titel".
function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)
  local number, title = text:match("^%s*Kapitel%s+(%d+)%s*[–%-]%s*(.+)%s*$")
  if not number then
    number, title = text:match("^%s*(%d+)%.%s+(.+)%s*$")
  end
  if not number then
    return nil
  end

  local title_tex = pandoc.write(
    pandoc.Pandoc({pandoc.Para(pandoc.read(title, "markdown").blocks[1].content)}),
    "latex"
  ):gsub("%s+$", "")

  return pandoc.RawBlock(
    "latex",
    "\\bookchapter{" .. number .. "}{" .. title_tex .. "}{" .. text .. "}"
  )
end
