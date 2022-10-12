-- Compute, for every country, the value of economic exchange, i.e., the difference between the number
-- of items from suppliers in that country sold to customers in other countries and the number of items
-- bought by local customers from foreign suppliers in 1994 (l shipdate

-- num items from supps in that country TO custs in other country
-- MINUS
-- num items bought by custs in that country FROM supps in other country

SELECT export_nat, sum_imp - sum_exp
FROM (SELECT n_name as export_nat, SUM(1) as sum_exp
    FROM orders, customer, lineitem, supplier, nation

    WHERE c_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1994%'

    GROUP BY n_name
),
    (SELECT n_name as import_nat, SUM(1) as sum_imp
    FROM orders, customer, lineitem, supplier, nation

    WHERE s_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1994%'

    GROUP BY n_name
)
WHERE export_nat = import_nat