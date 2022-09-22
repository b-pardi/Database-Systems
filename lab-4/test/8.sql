-- Find the number of distinct orders completed in 1995 by the suppliers in every nation. An order status
-- of F stands for complete. Print only those nations for which the number of orders is larger than 50

SELECT DISTINCT nation.n_name, COUNT(orders.o_orderkey)

FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
FROM
ON
FROM supplier
ON supplier.s_nationkey = nation.n_nationkey



WHERE substr(lineitem.l_receiptdate, 1, 4) = '1995'
AND COUNT(orders.o_orderkey) > 50