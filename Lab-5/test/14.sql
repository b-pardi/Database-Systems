-- For any two regions, find the gross discounted revenue (l extendedprice*(1-l discount)) derived
-- from line items in which parts are shipped from a supplier in the first region to a customer in the
-- second region in 1996 and 1997. List the supplier region, the customer region, the year (l shipdate),
-- and the revenue from shipments that took place in that yeaR

SELECT supp_reg_name, cust_reg_name, substr(date_96, 1, 4) as yr, revenue
FROM (SELECT supp_reg.r_name as supp_reg_name, cust_reg.r_name as cust_reg_name,
    line_96.l_shipdate as date_96,
    SUM(line_96.l_extendedprice*(1-line_96.l_discount)) as revenue
    FROM customer, supplier, orders,
    region as cust_reg,
    region as supp_reg,
    nation as cust_nat,
    nation as supp_nat,
    (SELECT *
    FROM lineitem
    WHERE l_shipdate LIKE '1996%') as line_96

    WHERE line_96.l_orderkey = o_orderkey
    AND o_custkey = c_custkey
    AND s_suppkey = line_96.l_suppkey
    AND s_nationkey = supp_nat.n_nationkey
    AND supp_nat.n_regionkey = supp_reg.r_regionkey
    AND c_nationkey = cust_nat.n_nationkey
    AND cust_nat.n_regionkey = cust_reg.r_regionkey
    GROUP BY supp_reg_name, cust_reg_name)

UNION

SELECT supp_reg_name, cust_reg_name, substr(date_97, 1, 4) as yr, revenue
FROM (SELECT supp_reg.r_name as supp_reg_name, cust_reg.r_name as cust_reg_name,
    line_97.l_shipdate as date_97,
    SUM(line_97.l_extendedprice*(1-line_97.l_discount)) as revenue
    FROM customer, supplier, orders,
    region as cust_reg,
    region as supp_reg,
    nation as cust_nat,
    nation as supp_nat,
    (SELECT *
    FROM lineitem
    WHERE l_shipdate LIKE '1997%') as line_97

    WHERE line_97.l_orderkey = o_orderkey
    AND o_custkey = c_custkey
    AND s_suppkey = line_97.l_suppkey
    AND s_nationkey = supp_nat.n_nationkey
    AND supp_nat.n_regionkey = supp_reg.r_regionkey
    AND c_nationkey = cust_nat.n_nationkey
    AND cust_nat.n_regionkey = cust_reg.r_regionkey
    GROUP BY supp_reg_name, cust_reg_name ) 

GROUP BY supp_reg_name, cust_reg_name, yr

/*
SELECT supp_reg_name, cust_reg_name, substr(l_shipdate, 1, 4), SUM(revenue)
FROM (SELECT supp_reg.r_name as supp_reg_name, cust_reg.r_name as cust_reg_name, l_shipdate,
    l_extendedprice*(1-l_discount) as revenue
    FROM lineitem, customer, supplier, orders,
    region as cust_reg,
    region as supp_reg,
    nation as cust_nat,
    nation as supp_nat

    WHERE l_orderkey = o_orderkey
    AND o_custkey = c_custkey
    AND s_suppkey = l_suppkey
    AND s_nationkey = supp_nat.n_nationkey
    AND supp_nat.n_regionkey = supp_reg.r_regionkey
    AND c_nationkey = cust_nat.n_nationkey
    AND cust_nat.n_regionkey = cust_reg.r_regionkey
    AND (l_shipdate LIKE '1996%' OR l_shipdate LIKE '1997%'))

GROUP BY supp_reg_name, cust_reg_name
*/