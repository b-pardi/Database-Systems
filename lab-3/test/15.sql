-- Find the total number of line items on orders with priority 3-MEDIUM supplied by suppliers from
-- GERMANY and FRANCE. Group these line items based on the year of the order from o orderdate. Print
-- the year and the count. Check the substr function in SQLite
SELECT strftime('%Y', orders.o_orderdate) as valYear, COUNT(lineitem.l_quantity)
FROM orders
JOIN lineitem
ON orders.o_orderkey = lineitem.l_orderkey
join supplier
ON supplier.s_suppkey = lineitem.l_suppkey
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey

WHERE (nation.n_name = 'FRANCE' OR nation.n_name = 'GERMANY')
AND (orders.o_orderpriority = '3-MEDIUM')

GROUP BY valYear