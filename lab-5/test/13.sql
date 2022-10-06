-- Count the number of orders made in the fourth quarter of 1997 in which at least one line item was
-- received by a customer earlier than its commit date. List the count of such orders for every order
-- priority

SELECT o_orderpriority, COUNT(l_orderkey)
FROM orders, lineitem,
    ( SELECT l_receiptdate, l_commitdate
    FROM lineitem as line2
    

WHERE o_orderkey = l_orderkey
AND 0 + strftime('%m', l_receiptdate) between 10 and 12 


GROUP BY o_orderpriority