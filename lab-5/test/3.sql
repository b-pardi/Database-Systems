-- For the line items ordered in October 1996 (o orderdate), find the smallest discount that is larger
-- than the average discount among all the orders.


SELECT min(l_discount)
FROM lineitem, orders
WHERE l_orderkey = o_orderkey
    AND o_orderdate LIKE '1996-10%'
    and l_discount >
        (select avg(o_discount)
        from
            (select l_orderkey, avg(l_discount) as o_discount
            from lineitem
            group by l_orderkey) sq1);