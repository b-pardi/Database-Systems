-- Find how many suppliers supply the most expensive part (p retailprice)

SELECT COUNT(s_suppkey)
FROM supplier, partsupp, part
WHERE s_suppkey = ps_suppkey
AND p_partkey = ps_partkey

AND p_retailprice = (SELECT MAX(p_retailprice) FROM part)