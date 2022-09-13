-- find the minimum account balance of the suppliers from nations with more than 5 suppliers. Print
-- the nation name, the number of suppliers from that nation, and the maximum account balance
SELECT DISTINCT nation.n_name, COUNT(supplier.s_nationkey), MIN(supplier.s_acctbal)
FROM supplier
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey

GROUP BY nation.n_name
HAVING COUNT(supplier.s_nationkey) > 5