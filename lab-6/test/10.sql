-- Find the region where customers spend the smallest amount of money (l extendedprice) buying items
-- from suppliers in the same region

SELECT r_name
FROM (SELECT r_name, MIN(sum_price)
    FROM (SELECT cust_reg.r_name, SUM(DISTINCT l_extendedprice) as sum_price
        FROM orders, customer, supplier, lineitem,
        nation as supp_nat,
        nation as cust_nat,
        region as supp_reg,
        region as cust_reg

        WHERE o_custkey = c_custkey
        AND c_nationkey = cust_nat.n_nationkey
        AND cust_nat.n_regionkey = cust_reg.r_regionkey
        AND o_orderkey = l_orderkey
        AND l_suppkey = s_suppkey
        AND s_nationkey = supp_nat.n_nationkey
        AND supp_nat.n_regionkey = supp_reg.r_regionkey
        AND supp_reg.r_name = cust_reg.r_name

        GROUP BY cust_reg.r_name
    ) sq
)