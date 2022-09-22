-- What is the maximum account balance for the suppliers in every nation? Print only those nations for
-- which the maximum balance is larger than 9000.

SELECT nation.n_name, MAX(supplier.s_acctbal)

FROM supplier
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey

WHERE supplier.s_acctbal > 9000

GROUP BY supplier.s_acctbal