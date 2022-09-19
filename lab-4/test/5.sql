-- Find the number of orders posted by every customer from GERMANY in 1993

SELECT customer.c_name, COUNT(orders.o_orderkey)

FROM customer
JOIN orders
ON customer.c_custkey = orders.o_custkey
JOIN nation
ON nation.n_nationkey = customer.c_nationkey

WHERE nation.n_name = 'GERMANY'
AND strftime('%Y', orders.o_orderdate) = '1993'

GROUP BY customer.c_name