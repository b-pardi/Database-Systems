-- How many customers and suppliers are in every country from AFRICA
/*
SELECT custs_nat.n_name, COUNT(DISTINCT c_name), COUNT(DISTINCT s_name)
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

SELECT cust_nat_name, COUNT(DISTINCT cust_tbl.c_name), COUNT(DISTINCT supp_tbl.s_name)
FROM (SELECT n_name as cust_nat_name, c_name
    FROM region, nation, customer
    WHERE c_nationkey = n_nationkey
    AND r_regionkey = n_regionkey
    AND r_name = 'AFRICA' ) cust_tbl,

    (SELECT n_name as supp_nat_name, s_name
    FROM region, nation, supplier
    WHERE s_nationkey = n_nationkey
    AND r_regionkey = n_regionkey
    AND r_name = 'AFRICA' ) supp_tbl

WHERE cust_nat_name = supp_nat_name
GROUP BY cust_nat_name