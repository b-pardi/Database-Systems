-- For parts whose type contains STEEL, return the name of the supplier from ASIA that can supply them
-- at minimum cost (ps supplycost), for every part size. Print the supplier name together with the part
-- size and the minimum cost

SELECT s_name, p_size, MIN(ps_supplycost)
FROM supplier, partsupp, part, nation, region

WHERE ps_partkey = p_partkey
AND ps_suppkey = s_suppkey
AND s_nationkey = n_nationkey
AND n_regionkey = r_regionkey

AND r_name = 'ASIA'
AND p_type LIKE '%STEEL%'

GROUP BY s_name
    
    /*(SELECT ps_supplycost
    FROM partsupp, supplier, nation, region
    WHERE ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'ASIA'*/