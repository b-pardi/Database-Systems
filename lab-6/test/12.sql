-- Find the nation(s) having customers that spend the smallest amount of money (o totalprice)

SELECT n_name
FROM (SELECT n_name, MIN(sum_price)
    FROM (SELECT n_name, SUM(o_totalprice) as sum_price
        FROM orders, customer, nation
        WHERE o_custkey = c_custkey
        AND c_nationkey = n_nationkey
        GROUP BY n_name
    ) sq
)