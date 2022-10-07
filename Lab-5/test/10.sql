-- How many customers from every region have never placed an order and have less than the average
-- account balance

SELECT r_name, COUNT(DISTINCT c_custkey)
FROM customer, region, nation,
    (SELECT r_name as avg_rname, AVG(c_acctbal) as avg_bal
    FROM customer, nation, region
    WHERE c_nationkey = n_nationkey
    AND n_regionkey = r_regionkey )

WHERE c_custkey NOT IN
    (SELECT DISTINCT o_custkey
        FROM orders)
    
AND c_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND c_acctbal < avg_bal

GROUP BY r_name

