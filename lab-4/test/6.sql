-- How many unique parts produced by every supplier in CANADA are ordered at every priority? Print the
-- supplier name, the order priority, and the number of parts
SELECT supplier.s_name, orders.o_orderpriority, COUNT(DISTINCT partsupp.ps_partkey)
/*
FROM supplier
JOIN partsupp
ON supplier.s_suppkey = partsupp.ps_suppkey
JOIN part
ON partsupp.ps_partkey = part.p_partkey
JOIN nation
ON nation.n_nationkey = supplier.s_nationkey
JOIN lineitem
ON part.p_partkey = lineitem.l_partkey
JOIN orders
ON orders.o_orderkey = lineitem.l_orderkey
*/

FROM orders
JOIN lineitem
ON orders.o_orderkey = lineitem.l_orderkey
JOIN partsupp
ON partsupp.ps_partkey = lineitem.l_partkey
JOIN supplier
ON lineitem.l_suppkey = supplier.s_suppkey
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey

WHERE nation.n_name = 'CANADA'

GROUP BY supplier.s_name, orders.o_orderpriority