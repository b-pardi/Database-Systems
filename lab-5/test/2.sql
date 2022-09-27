-- How many suppliers in every region have less balance in their account than the average account balance
-- of their own region?

SELECT r_name, COUNT(s_suppkey)

FROM supplier, nation, region

WHERE s_nationkey = n_nationkey
AND n_regionkey = r_regionkey

GROUP BY r_name

HAVING s_acctbal < AVG(s_acctbal)