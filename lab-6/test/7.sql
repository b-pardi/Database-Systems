-- Find how many suppliers have less than 50 distinct orders from customers in GERMANY and FRANCE
-- together

SELECT COUNT(DISTINCT supp_sq.s_suppkey)
FROM (SELECT s_suppkey, o_orderkey
    FROM supplier, orders, customer, lineitem, nation
    WHERE s_suppkey = l_suppkey
    AND l_orderkey = o_orderkey
    AND o_custkey = c_custkey
    AND c_nationkey = n_nationkey

    AND (n_name = 'FRANCE' OR n_name = 'GERMANY')
    GROUP BY o_orderkey
    HAVING COUNT(o_orderkey) < 50
) as supp_sq