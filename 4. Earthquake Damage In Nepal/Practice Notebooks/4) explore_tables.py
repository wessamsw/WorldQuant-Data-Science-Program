%%sql
SELECT distinct(district_id)    # gives unique values of column district_id
FROM id_map   # name of table


# num of observations in table id_map
# where value of column district_id is 1
%%sql
SELECT count(*)
FROM id_map
WHERE district_id = 1
