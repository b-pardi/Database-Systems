-- How many orders are posted by customers in every country in AMERICA

SELECT nation.n_name, COUNT(*)

FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
JOIN nation
ON nation.n_nationkey = customer.c_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

WHERE region.r_name = 'AMERICA'

GROUP BY nation.n_name