-- For the line items ordered in October 1996 (o orderdate), find the smallest discount that is larger
-- than the average discount among all the orders.


SELECT min(l_discount)
FROM lineitem, orders
WHERE l_orderkey = o_orderkey

AND o_orderdate LIKE '1996-10%'
AND l_discount >
    (SELECT avg(o_discount)
    FROM
        (SELECT l_orderkey, avg(l_discount) as o_discount
        FROM lineitem
        GROUP BY l_orderkey) sq1);