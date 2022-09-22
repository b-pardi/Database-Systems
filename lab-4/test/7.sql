-- How many orders do customers in every nation in AMERICA have in every status? Print the nation
-- name, the order status, and the count

SELECT nation.n_name, orders.o_orderstatus, COUNT(orders.o_orderstatus)

FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
JOIN nation
ON customer.c_nationkey = nation.n_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

WHERE region.r_name = 'AMERICA'

GROUP BY nation.n_name, orders.o_orderstatus