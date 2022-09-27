-- For the line items ordered in October 1996 (o orderdate), find the smallest discount that is larger
-- than the average discount among all the orders.

SELECT MIN(l_discount)

FROM lineitem, orders

WHERE l_orderkey = o_orderkey
AND o_orderdate LIKE '1996-10%'

GROUP BY 
HAVING l_discount > AVG(l_discount)