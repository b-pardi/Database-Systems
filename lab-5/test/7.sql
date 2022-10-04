-- For every order priority, count the number of parts ordered in 1997 and received later (l receiptdate)
-- than the commit date (l commitdate)

SELECT o_orderpriority, COUNT(*)
FROM (
    SELECT *
    FROM lineitem, part, orders
    WHERE l_orderkey = o_orderkey
    AND p_partkey = l_partkey
    AND o_orderdate LIKE '1997%'
    AND l_receiptdate > l_commitdate )
GROUP BY o_orderpriority