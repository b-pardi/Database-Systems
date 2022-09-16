-- Find the total account balance of all the customers from ASIA in the MACHINERY market segment
SELECT SUM(DISTINCT customer.c_acctbal)
--SELECT customer.c_name, orders.o_custkey, customer.c_custkey, customer.c_nationkey, nation.n_nationkey, nation.n_regionkey, region.r_regionkey, region.r_name, customer.c_mktsegment

FROM customer
JOIN nation
ON customer.c_nationkey = nation.n_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

WHERE region.r_name = 'ASIA'
AND customer.c_mktsegment = 'MACHINERY'

/*
FROM customer, orders, nation, region
WHERE orders.o_custkey = customer.c_custkey
AND customer.c_nationkey = nation.n_nationkey
AND nation.n_regionkey = region.r_regionkey
AND region.r_name = 'ASIA'
AND customer.c_mktsegment = 'MACHINERY'
*/