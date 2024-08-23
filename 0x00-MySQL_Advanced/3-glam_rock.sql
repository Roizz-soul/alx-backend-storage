-- Script to list stuff
-- SQL script to list Glam rock bands ranked by their longevity
-- Select band_name and lifespan from metal band table
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
