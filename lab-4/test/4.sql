-- How many parts with size below 20 does every supplier from CANADA offer? Print the name of the
-- supplier and the number of parts

SELECT supplier.s_name, COUNT(supplier.s_name)

FROM supplier
JOIN partsupp
ON supplier.s_suppkey = partsupp.ps_suppkey
JOIN part
ON partsupp.ps_partkey = part.p_partkeY
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey

WHERE part.p_size < 20
AND nation.n_name = 'CANADA'

GROUP BY supplier.s_name