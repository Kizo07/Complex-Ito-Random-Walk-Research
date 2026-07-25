-- Preserve vector figure sources for PDF while serving browser-friendly PNG
-- companions in HTML. Only project-generated publication figures are changed.
function Image(image)
  if FORMAT:match("html") then
    image.src = image.src:gsub(
      "^figures/vector/(.+)%.pdf$",
      "figures/raster/%1.png"
    )
  end
  return image
end
