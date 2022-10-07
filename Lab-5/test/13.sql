-- Count the number of orders made in the fourth quarter of 1997 in which at least one line item was
-- received by a customer earlier than its commit date. List the count of such orders for every order
-- priority

SELECT o_orderpriority, COUNT(DISTINCT o_orderkey)
FROM orders, lineitem

WHERE o_orderkey = l_orderkey
AND o_orderdate LIKE '1997%'
AND 0 + strftime('%m', o_orderdate) between 10 and 12

AND o_orderkey IN (SELECT o_orderkey
    FROM lineitem, orders
    WHERE l_orderkey = o_orderkey
    AND date(l_receiptdate) < date(l_commitdate) )

GROUP BY o_orderpriority