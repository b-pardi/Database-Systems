-- How many line items are supplied by suppliers in AFRICA for orders made by customers in UNITED
-- STATES?
/*
SELECT COUNT(DISTINCT orders.o_orderkey)

FROM supplier
JOIN nation as supplier_nation
ON supplier.s_nationkey = supplier_nation.n_nationkey
JOIN region as supplier_region
ON supplier_nation.n_regionkey = supplier_region.r_regionkey

JOIN customer, nation as customer_nation
ON customer_nation.n_nationkey = customer.c_nationkey
JOIN orders
ON customer.c_custkey = orders.o_custkey
JOIN lineitem
ON orders.o_orderkey = lineitem.l_orderkey

WHERE supplier_region.r_name = 'AFRICA'
AND customer_nation.n_name = 'UNITED STATES'
*/

SELECT COUNT(orders.o_orderkey)
FROM supplier,
customer,
nation as cn,
nation as sn,
region as sr,
orders,
lineitem

WHERE s_nationkey = sn.n_nationkey 
AND sn.n_regionkey = sr.r_regionkey
AND sr.r_name = 'AFRICA'
AND s_suppkey = l_suppkey
AND l_orderkey = o_orderkey
AND o_custkey = c_custkey
AND c_nationkey = cn.n_nationkey
AND cn.n_name = 'UNITED STATES';