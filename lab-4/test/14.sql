-- List the maximum total price of an order between any two regions, i.e., the suppliers are from one
-- region and the customers are from the other region

/*
FROM orders
JOIN customer
ON orders.custkey = customer.custkey

JOIN customer, nation as customer_nation
ON customer_nation.n_nationkey = customer.c_nationkey
JOIN customer_nation, region as customer_region
ON customer_nation.n_regionkey = customer_region.r_regionkey

JOIN supplier, nation as supplier_nation
ON supplier.s_nationkey = supplier_nation.n_nationkey
JOIN supplier_nation, region as supplier_region
ON supplier_nation.n_regionkey = supplier_region.r_regionkey
*/
SELECT supp_reg.r_name, cust_reg.r_name, MAX(orders.o_totalprice)

FROM orders,
customer,
supplier,
nation as cust_nat,
nation as supp_nat,
region as cust_reg,
region as supp_reg

WHERE s_nationkey = supp_nat.n_nationkey
AND supp_nat.n_regionkey = supp_reg.r_regionkey
AND c_nationkey = cust_nat.n_nationkey
AND cust_nat.n_regionkey = cust_reg.r_regionkey

AND o_custkey = c_custkey


GROUP BY supp_reg.r_name, cust_reg.r_name