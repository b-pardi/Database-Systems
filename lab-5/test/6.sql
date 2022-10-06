-- Based on the available quantity of items, who is the manufacturer p mfgr of the most popular item
-- (the more popular an item is, the less available it is in ps availqty) from Supplier#000000010

SELECT p_mfgr
FROM part, partsupp
WHERE p_partkey = ps_partkey

AND ps_availqty IN
    (SELECT MIN(ps_availqty)
    FROM partsupp, part, supplier
    WHERE ps_suppkey = s_suppkey
    AND ps_partkey = p_partkey
    AND s_name = 'Supplier#000000010')