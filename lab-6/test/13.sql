-- Find the nation(s) with the most developed industry, i.e., selling items totaling the largest amount of
-- money (l extendedprice) in 1994 (l shipdate

SELECT n_name
FROM (SELECT n_name, MAX(sum_price)
    FROM (SELECT n_name, SUM(l_extendedprice) as sum_price
        FROM lineitem, supplier, nation
        WHERE l_suppkey = s_suppkey
        AND s_nationkey = n_nationkey

        AND l_shipdate LIKE '1994%'
        GROUP BY n_name
    ) sq
)