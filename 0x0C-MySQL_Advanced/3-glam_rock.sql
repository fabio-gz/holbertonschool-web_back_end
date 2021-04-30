--all glam rock bands
SELECT band_name, (IFNULL(split,2021)-formed) AS lifespan FROM metal_bands
WHERE style LIKE "%Glam rock%" ORDER BY lifespan DESC;
