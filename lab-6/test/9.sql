-- Find the distinct parts (p name) ordered by customers from AMERICA that are supplied by exactly 3
-- suppliers from ASIA

SELECT DISTINCT p_name
    FROM part, lineitem, orders, customer, nation, region
    WHERE o_orderkey = l_orderkey
    AND c_custkey = o_custkey
    AND l_partkey = p_partkey
    AND c_nationkey = n_nationkey
    AND n_regionkey = r_regionkey

    AND r_name = 'AMERICA'

    AND p_partkey IN (SELECT DISTINCT l_partkey
        FROM lineitem, supplier, nation, region
        WHERE s_suppkey = l_suppkey
        AND s_nationkey = n_nationkey
        AND n_regionkey = r_regionkey

        AND r_name = 'ASIA'
        GROUP BY l_partkey
        HAVING COUNT(s_suppkey) = 3
    )
    

/*
SELECT p_name
FROM partsupp, supplier, nation, region, part

WHERE ps_suppkey = s_suppkey
AND p_partkey = ps_partkey
AND s_nationkey = n_nationkey
AND n_regionkey = r_regionkey

AND p_partkey IN (SELECT l_partkey
    FROM orders, lineitem, 

    WHERE 
)*/