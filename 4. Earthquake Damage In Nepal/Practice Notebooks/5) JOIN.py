%%sql
# joining tables at columns building_id
SELECT distinct(i.building_id) AS b_id,   # building_id column of table i aliased as b_id
     s.*,     # selects all columns of table s
     d.damage_grade   # select damage_grade column of table d
FROM id_map AS i
JOIN building_structure AS s ON i.building_id = s.building_id
JOIN building_damage AS d ON i.building_id = d.building_id
WHERE district_id = 3
LIMIT 5
