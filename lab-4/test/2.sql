-- Find the number of suppliers from every region.

SELECT region.r_name, COUNT(*)

FROM supplier
JOIN nation
ON supplier.s_nationkey = nation.n_nationkey
JOIN region
ON region.r_regionkey = nation.n_regionkey

GROUP BY region.r_name