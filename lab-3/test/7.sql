-- How many line items did Customer#000000020 order? Print the number of ordered line items
-- corresponding to every (year, month) pair
SELECT substr(lineitem.l_receiptdate, 1, 7), COUNT(*)
FROM lineitem
JOIN orders
ON lineitem.l_orderkey = orders.o_orderkey
JOIN customer
ON orders.o_custkey = customer.c_custkey

WHERE customer.c_name = 'Customer#000000020'
GROUP BY substr(lineitem.l_receiptdate, 1, 7)