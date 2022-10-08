-- The market share for a given nation within a given region is defined as the fraction of the revenue from
-- the line items ordered by customers in the given region that are supplied by suppliers from the given
-- nation. The revenue of a line item is defined as l extendedprice*(1-l discount). Determine the
-- market share of UNITED STATES in ASIA in 1997 (l shipdate)

-- find revenue from line items ordered by cust in given reg supplied by suppliers from given nat
-- rev def as l_extendedprice*(1-l_discount)
-- of us in asia in 1997 (l_shipdate)
/*
SELECT us_revenue / total_revenue
FROM (SELECT SUM(DISTINCT l_extendedprice*(1-l_discount)) as us_revenue,
    cust_nat.n_name, supp_reg.r_name
    FROM customer, orders, lineitem, supplier,
    nation as cust_nat,
    nation as supp_nat,
    region as cust_reg,
    region as supp_reg
    WHERE c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND s_suppkey = l_suppkey
    AND s_nationkey = supp_nat.n_nationkey
    AND supp_nat.n_regionkey = supp_reg.r_regionkey
    AND c_nationkey = cust_nat.n_nationkey
    AND cust_nat.n_regionkey = cust_reg.r_regionkey

    --AND cust_nat.n_name = 'UNITED STATES'
    --AND supp_reg.r_name = 'ASIA'
    AND cust_reg.r_name = 'ASIA'

    AND l_shipdate LIKE '1997%' ) ,

    (SELECT SUM(DISTINCT l_extendedprice*(1-l_discount)) as total_revenue,
    cust_nat.n_name, supp_reg.r_name
    FROM customer, orders, lineitem, supplier,
    nation as cust_nat,
    nation as supp_nat,
    region as cust_reg,
    region as supp_reg
    WHERE c_custkey = o_custkey
    AND l_orderkey = o_orderkey
    AND s_suppkey = l_suppkey
    AND s_nationkey = supp_nat.n_nationkey
    AND supp_nat.n_regionkey = supp_reg.r_regionkey
    AND c_nationkey = cust_nat.n_nationkey
    AND cust_nat.n_regionkey = cust_reg.r_regionkey

    --AND cust_nat.n_name <> 'UNITED STATES'
    --AND supp_reg.r_name = 'ASIA'
    AND l_shipdate LIKE '1997%')
    */

SELECT us_market_share / total_market_share
    FROM (SELECT SUM(l_extendedprice*(1-l_discount)) as total_market_share
    FROM orders, customer, region, nation, lineitem
    WHERE o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND c_nationkey = n_nationkey
    AND n_regionkey = r_regionkey
    AND r_name = 'ASIA'
    AND l_shipdate LIKE '1997%') tm,

    (SELECT SUM(l_extendedprice*(1-l_discount)) as us_market_share
    FROM orders, customer, region, nation as cust_nat, nation as supp_nat,
    lineitem, supplier
    WHERE o_custkey = c_custkey
    AND l_orderkey = o_orderkey
    AND c_nationkey = cust_nat.n_nationkey
    AND l_suppkey = s_suppkey
    AND s_nationkey = supp_nat.n_nationkey
    AND cust_nat.n_regionkey = r_regionkey
    AND supp_nat.n_name = 'UNITED STATES'
    AND r_name = 'ASIA'
    AND l_shipdate LIKE '1997%') usm;
