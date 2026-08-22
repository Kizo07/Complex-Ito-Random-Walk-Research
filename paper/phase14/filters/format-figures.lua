-- Preserve vector figures in PDF while serving browser-friendly raster
-- companions in HTML.
function Image(image)
  if FORMAT:match("html") then
    image.src = image.src:gsub(
      "^figures/vector/(.+)%.pdf$",
      "figures/raster/%1.png"
    )
  end
  return image
end
