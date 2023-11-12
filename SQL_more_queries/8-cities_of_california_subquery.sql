-- Select the id and name of the cities that have california as name
SELECT id, name FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
) ORDER BY id;