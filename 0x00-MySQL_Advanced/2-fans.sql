-- Script for ranking country origins by number of fans
-- Select script
SELECT 
    origin, 
    SUM(fans) AS nb_fans
FROM 
    metal_bands
GROUP BY 
    origin
ORDER BY 
    nb_fans DESC;
