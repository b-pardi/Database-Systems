-- Find the name of the suppliers from EUROPE who have more than $7000 on account balance. Print the
-- supplier name and their account balance
SELECT supplier.s_name, supplier.s_acctbal
FROM supplier
JOIN nation
ON nation.n_nationkey = supplier.s_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

WHERE region.r_regionkey = 3
AND supplier.s_acctbal > 7000;