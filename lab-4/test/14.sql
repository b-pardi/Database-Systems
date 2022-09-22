-- List the maximum total price of an order between any two regions, i.e., the suppliers are from one
-- region and the customers are from the other region

SELECT supp_reg.r_name, cust_reg.r_name, MAX(o_totalprice)

FROM orders,
customer,
supplier,
lineitem,
nation as cust_nat,
nation as supp_nat,
region as cust_reg,
region as supp_reg

WHERE s_nationkey = supp_nat.n_nationkey
AND supp_nat.n_regionkey = supp_reg.r_regionkey
AND c_nationkey = cust_nat.n_nationkey
AND cust_nat.n_regionkey = cust_reg.r_regionkey

AND o_custkey = c_custkey
AND s_suppkey = l_suppkey
AND l_orderkey = o_orderkey

GROUP BY supp_reg.r_name, cust_reg.r_name