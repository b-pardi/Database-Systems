-- Find the number of orders having status P. Group these orders based on the region of the customer
-- who posted the order. Print the region name and the number of status P orders
SELECT region.r_name, COUNT(orders.o_orderstatus)

FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
JOIN nation
ON customer.c_nationkey = nation.n_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

WHERE orders.o_orderstatus = 'P'
GROUP BY region.r_name