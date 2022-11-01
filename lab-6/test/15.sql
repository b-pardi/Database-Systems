-- Compute the change in the economic exchange for every country between 1994 and 1996. There should
-- be two columns in the output for every country: 1995 and 1996. Hint: use CASE to select the values
-- in the result
-- select n_name, difference_economic_exchange95_94, 
--  n_name, difference_economic_exchange96_95

SELECT n_name, yr_exp_sum-yr_imp_sum
    FROM (SELECT export_tbl.n_name, yr_exp_sum, yr_imp_sum
    FROM (SELECT n_name,
        CASE
            WHEN l_shipdate LIKE '1996%' THEN SUM(1)
            WHEN l_shipdate LIKE '1995%' THEN SUM(1)
            WHEN l_shipdate LIKE '1994%' THEN SUM(1)
        ELSE
            SUM(0)
        END yr_exp_sum
        FROM orders, customer, lineitem, supplier, nation

        WHERE c_nationkey = n_nationkey
        AND o_custkey = c_custkey
        AND l_orderkey = o_orderkey
        AND l_suppkey = s_suppkey
        AND c_nationkey <> s_nationkey
        GROUP BY n_name, substr(l_shipdate, 1, 4)
    ) export_tbl,
        (SELECT n_name,
        CASE
            WHEN l_shipdate LIKE '1996%' THEN SUM(1)
            WHEN l_shipdate LIKE '1995%' THEN SUM(1)
            WHEN l_shipdate LIKE '1994%' THEN SUM(1)
        ELSE
            SUM(0)
        END yr_imp_sum
        FROM orders, customer, lineitem, supplier, nation

        WHERE s_nationkey = n_nationkey
        AND o_custkey = c_custkey
        AND l_orderkey = o_orderkey
        AND l_suppkey = s_suppkey
        AND c_nationkey <> s_nationkey
        GROUP BY n_name, substr(l_shipdate, 1, 4)
    ) import_tbl

    WHERE import_tbl.n_name = export_tbl.n_name
    AND import_tbl.imp
)
/*
SELECT export_nat96, tot_exc95 - tot_exc94, tot_exc96 - tot_exc95
FROM (SELECT export_nat96, imp_exc96 - exp_exc96 as tot_exc96,
    imp_exc95 - exp_exc95 as tot_exc95,
    imp_exc94 - exp_exc94 as tot_exc94
FROM (SELECT n_name as export_nat96, SUM(1) as exp_exc96
    FROM orders, customer, lineitem, supplier, nation

    WHERE c_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1996%'

    GROUP BY n_name
),
    (SELECT n_name as import_nat96, SUM(1) as imp_exc96
    FROM orders, customer, lineitem, supplier, nation

    WHERE s_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1996%'

    GROUP BY n_name
),
(SELECT n_name as export_nat95, SUM(1) as exp_exc95
    FROM orders, customer, lineitem, supplier, nation

    WHERE c_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1995%'

    GROUP BY n_name
),
    (SELECT n_name as import_nat95, SUM(1) as imp_exc95
    FROM orders, customer, lineitem, supplier, nation

    WHERE s_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1995%'

    GROUP BY n_name
),
(SELECT n_name as export_nat94, SUM(1) as exp_exc94
    FROM orders, customer, lineitem, supplier, nation

    WHERE c_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1994%'

    GROUP BY n_name
),
    (SELECT n_name as import_nat94, SUM(1) as imp_exc94
    FROM orders, customer, lineitem, supplier, nation

    WHERE s_nationkey = n_nationkey
    AND o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND l_suppkey = s_suppkey
    AND c_nationkey <> s_nationkey
    AND l_shipdate LIKE '1994%'

    GROUP BY n_name
)

WHERE export_nat96 = import_nat96
AND export_nat95 = import_nat95
AND export_nat95 = export_nat96
AND export_nat94 = import_nat94
AND export_nat94 = export_nat96
)*/