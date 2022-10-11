-- Find how many distinct customers have at least one order supplied exclusively by suppliers from
-- AMERICA.

SELECT COUNT(DISTINCT order_sq.c_custkey)
FROM (SELECT c_custkey
    FROM customer, orders, lineitem, supplier, nation
    WHERE c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND s_nationkey = n_nationkey

    AND o_orderkey NOT IN (SELECT DISTINCT o_orderkey
        FROM orders, lineitem, supplier, nation
        WHERE o_orderkey = l_orderkey
        AND l_suppkey = s_suppkey
        AND s_nationkey = n_nationkey

        AND n_name <> 'UNITED STATES'
    )
) order_sq