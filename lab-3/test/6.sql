-- What are the nations of the customers that made orders between September 9-11, 1994? Print every
-- nation only once and sort them in alphabetical order
SELECT DISTINCT nation.n_name

FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
JOIN nation
ON customer.c_nationkey = nation.n_nationkey

WHERE o_orderdate BETWEEN '1994-09-09' AND '1994-09-11'
ORDER BY nation.n_name ASC