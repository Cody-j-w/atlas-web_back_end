-- script for counting the number of metal fans and grouping them by country
SOURCE metal_bands.sql

SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY SUM(fans) DESC;
