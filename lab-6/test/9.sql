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

    AND p_partkey IN (SELECT DISTINCT ps_partkey--, r_name, s_suppkey
        FROM partsupp, supplier, nation, region
        WHERE ps_suppkey = s_suppkey
        AND s_nationkey = n_nationkey
        AND n_regionkey = r_regionkey

        AND r_name = 'ASIA'
        GROUP BY ps_partkey
        HAVING COUNT(s_suppkey) = 3
    )