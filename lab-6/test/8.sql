-- Find how many distinct customers have at least one order supplied exclusively by suppliers from
-- AMERICA.
/*
SELECT COUNT(DISTINCT order_sq.c_custkey)
FROM (SELECT c_custkey
    FROM customer, orders
    WHERE c_custkey = o_custkey

    AND o_orderkey NOT IN (SELECT DISTINCT p_partkey
        FROM orders, lineitem, supplier, nation
        WHERE o_orderkey = l_orderkey
        AND l_suppkey = s_suppkey
        AND s_nationkey = n_nationkey

        AND n_name <> 'UNITED STATES'
    )
) order_sq
*/
/*
SELECT DISTINCT l_partkey
FROM orders, lineitem
WHERE l_orderkey = o_orderkey
ORDER BY l_partkey

AND l_partkey IN (SELECT DISTINCT ps_partkey
    FROM partsupp, supplier, nation
    WHERE ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    ORDER BY ps_partkey
)
*/

SELECT COUNT(DISTINCT c_custkey)
FROM customer, orders, lineitem, supplier, nation, region
WHERE c_custkey = o_custkey
AND l_orderkey = o_orderkey
AND s_suppkey = l_suppkey
AND s_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND r_name = 'AMERICA'


AND l_orderkey NOT IN (SELECT DISTINCT l_orderkey
    FROM lineitem, supplier, nation, orders, region
    WHERE l_suppkey = s_suppkey
    AND l_orderkey = o_orderkey
    AND s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name <> 'AMERICA'
)