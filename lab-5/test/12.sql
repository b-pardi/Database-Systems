-- What is the total supply cost (ps supplycost) for parts less expensive than $1000 (p retailprice) shipped
-- in 1997 (l shipdate) by suppliers who did not supply any line item with an extended price less than
-- 2000 in 1996

SELECT SUM(ps_supplycost)
FROM partsupp, part, lineitem, supplier

WHERE l_partkey = p_partkey
AND p_partkey = ps_partkey
AND ps_suppkey = s_suppkey

AND p_retailprice < 1000
AND l_shipdate LIKE '1997%'

AND s_suppkey NOT IN
    (SELECT DISTINCT s_suppkey
    FROM supplier as sup2, 
        ( SELECT DISTINCT line3.l_suppkey, l_extendedprice
        FROM lineitem as line3
        WHERE line3.l_shipdate LIKE '1996%' ) yr_tbl
    WHERE yr_tbl.l_suppkey = sup2.s_suppkey
    AND yr_tbl.l_extendedprice < 2000 )


