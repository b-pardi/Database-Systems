-- Find the supplier with the largest account balance in every region. Print the region name, the supplier
-- name, and the account balance

SELECT region.r_name, supplier.s_name, MAX(supplier.s_acctbal)

FROM supplier
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey
JOIN region
ON nation.n_regionkey = region.r_regionkey

GROUP BY region.r_name