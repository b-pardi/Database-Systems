-- How many line items did Customer#000000020 order? Print the number of ordered line items
-- corresponding to every (year, month) pair
SELECT SUM(lineitem.l_quantity)
FROM lineitem
JOIN orders
ON lineitem.l_orderkey = orders.o_orderkey
JOIN customer
ON orders.o_custkey = customer.c_custkey

WHERE c_name = 'Customer#000000020'

