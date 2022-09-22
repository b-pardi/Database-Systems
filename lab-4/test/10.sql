-- Find the minimum and maximum discount for every part having ECONOMY and COPPER in its type.

SELECT part.p_type, MIN(lineitem.l_discount), MAX(lineitem.l_discount)

FROM part
JOIN partsupp
ON part.p_partkey = partsupp.ps_partkey
JOIN lineitem
ON partsupp.ps_partkey = lineitem.l_partkey

WHERE part.p_type LIKE '%ECONOMY%'
AND part.p_type LIKE '%COPPER%'

GROUP BY part.p_type