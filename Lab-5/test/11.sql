-- Find the lowest value line item(s) (l extendedprice*(1-l discount)) shipped after October 2,
-- 1996. Print the name of the part corresponding to these line item(s)

SELECT p_name
FROM lineitem, part,
    ( SELECT MIN(l_extendedprice*(1-l_discount)) as lowest_val
    FROM lineitem ) min_tbl

WHERE l_partkey = p_partkey
AND date(l_shipdate) > ('1996-10-2')
AND l_extendedprice*(1-l_discount) = lowest_val