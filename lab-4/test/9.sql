-- How many different order clerks did the suppliers in UNITED STATES work with?

SELECT COUNT(DISTINCT orders.o_clerk)

FROM orders
JOIN lineitem
ON orders.o_orderkey = lineitem.l_orderkey
JOIN partsupp
ON lineitem.l_suppkey = partsupp.ps_suppkey
JOIN supplier
ON partsupp.ps_suppkey = supplier.s_suppkey
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey

WHERE nation.n_name = 'UNITED STATES'