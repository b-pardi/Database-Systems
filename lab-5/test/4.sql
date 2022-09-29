-- How many customers and suppliers are in every country from AFRICA
/*
SELECT custs_nat.n_name, supps_nat.n_name, COUNT(DISTINCT c_name), COUNT(DISTINCT s_name)
FROM customer, supplier,
nation as custs_nat,
nation as supps_nat,
region as custs_reg,
region as supps_reg

WHERE c_nationkey = custs_nat.n_nationkey
AND custs_nat.n_regionkey = custs_reg.r_regionkey
AND s_nationkey = supps_nat.n_nationkey
AND supps_nat.n_regionkey = supps_reg.r_regionkey

AND custs_reg.r_name = 'AFRICA'
AND supps_reg.r_name = 'AFRICA'

GROUP BY custs_nat.n_name, supps_nat.n_name
*/

SELECT n_name, COUNT(DISTINCT c_name), COUNT(DISTINCT s_name)
FROM customer, supplier,
nation as custs_nat,
nation as supps_nat,
region as custs_reg,
region as supps_reg