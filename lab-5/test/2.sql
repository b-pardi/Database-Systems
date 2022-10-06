-- How many suppliers in every region have less balance in their account than the average account balance
-- of their own region?

SELECT r_name, COUNT(s_suppkey)

FROM supplier, nation, region,
    (SELECT r_name as avg_rname, AVG(s_acctbal) as avg_bal
    FROM supplier, nation, region
    WHERE s_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    GROUP BY r_name) avg_tbl

WHERE s_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND avg_tbl.avg_rname = r_name
AND s_acctbal < avg_bal
    

GROUP BY r_name
