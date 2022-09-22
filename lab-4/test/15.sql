-- How many distinct orders are between customers with positive account balance and suppliers with
-- negative account balance

SELECT COUNT(DISTINCT o_totalprice)
FROM orders,
lineitem,
customer,
supplier

WHERE o_custkey = c_custkey
AND o_orderkey = l_orderkey
AND l_suppkey = s_suppkey

AND c_acctbal > 0
AND s_acctbal < 0