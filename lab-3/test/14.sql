-- Find how many 1-URGENT priority orders have been posted by customers from PERU between 1995 and
-- 1997, combined
SELECT COUNT(orders.o_orderpriority)
FROM orders
JOIN customer
ON orders.o_custkey = customer.c_custkey
JOIN nation
ON customer.c_nationkey = nation.n_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

WHERE nation.n_name = 'PERU'
AND orders.o_orderpriority = '1-URGENT'
AND orders.o_orderdate BETWEEN '1995-01-01T00:00:00.000' AND '1997-12-31T00:00:00.000'