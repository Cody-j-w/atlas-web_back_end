-- script for listing glam rock bands by lifetime
SOURCE metal_bands.sql

SELECT band_name, TIMESTAMPDIFF(year, MAKEDATE(formed, 1), IF(split IS NULL, CURDATE(), MAKEDATE(split, 1))) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
