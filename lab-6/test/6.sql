-- Find the supplier-customer pair(s) with the least expensive (o totalprice) order(s) completed (F in
-- o orderstatus). Print the supplier name, the customer name, and the total price

SELECT cheap.s_name, cheap.c_name, MIN(cheap.o_totalprice)
FROM (SELECT s_name, c_name, o_totalprice
    FROM supplier, customer, orders, lineitem
    WHERE o_orderkey = l_orderkey
    AND l_suppkey = s_suppkey
    AND o_custkey = c_custkey

    AND o_orderstatus = 'F'
    GROUP BY o_totalprice
) as cheap