-- Find the total price o totalprice of orders made by customers from ASIA in 1997.
SELECT SUM(orders.o_totalprice)
FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
JOIN nation
ON nation.n_nationkey = customer.c_nationkey
JOIN region
ON region.r_regionkey = nation.n_nationkey

WHERE region.r_name = 'ASIA'
AND orders.o_orderdate BETWEEN '1997-01-01T00:00:00.000' AND '1997-12-31T00:00:00.000'