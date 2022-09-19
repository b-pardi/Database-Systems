-- Find the total price paid on orders by every customer from FRANCE in 1995. Print the customer name
-- and the total price

SELECT customer.c_name, SUM(orders.o_totalprice)

FROM customer
JOIN orders
ON customer.c_custkey = orders.o_custkey
JOIN nation
ON customer.c_nationkey = nation.n_nationkey

WHERE nation.n_name = 'FRANCE'
AND strftime('%Y', orders.o_orderdate) = '1995'

GROUP BY customer.c_name