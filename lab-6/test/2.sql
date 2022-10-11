-- Find the number of customers who had at least three orders in November 1995 (o orderdate)

SELECT COUNT(sq_orders.c_custkey)
FROM (SELECT c_custkey
    FROM customer, orders
    WHERE o_custkey = c_custkey
    AND o_orderdate LIKE '1995-11%'
    GROUP BY c_custkey
    HAVING COUNT(c_custkey) > 2) as sq_orders