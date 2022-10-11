-- Find the region where customers spend the smallest amount of money (l extendedprice) buying items
-- from suppliers in the same region

SELECT r_name
FROM (SELECT n_name, MIN(sum_price)
    FROM (SELECT n_name, SUM(o_total) as sum_price
        FROM orders, customer, nation, region
        WHERE o_custkey = c_custkey
        AND c_nationkey = n_nationkey
        AND 
        GROUP BY r_name
    ) sq
)