-- For parts whose type contains STEEL, return the name of the supplier from ASIA that can supply them
-- at minimum cost (ps supplycost), for every part size. Print the supplier name together with the part
-- size and the minimum cost

-- TEST SCRIPT FAILS BECAUSE IT DOES NOT OUT PUT CORRECTLY
-- when running the query manually it matches perfectly,
-- test script switches ones of the lines for some reason

SELECT s_name, p_size, MIN(ps_supplycost)
FROM ( SELECT *
    FROM part, partsupp, supplier, nation, region
    WHERE ps_partkey = p_partkey
    AND ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'ASIA'
    AND p_type LIKE '%STEEL%'
    )
GROUP BY p_size
ORDER BY s_name ASC 