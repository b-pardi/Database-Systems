-- for each supplier, find 2 nations with largest number
-- of lineitems supplied by supplier
-- that are ordered by customers from that nation






/*
select s_name, supp_nat.n_name, sum(l_quantity) as q
from supplier, customer, orders, lineitem,
nation as supp_nat,
nation as cust_nat

where s_suppkey = l_suppkey
and l_orderkey = o_orderkey
and c_custkey = o_custkey
and supp_nat.n_nationkey = s_nationkey
and cust_nat.n_nationkey = c_nationkey

and s_name = 'Supplier#000000001'

group by supp_nat.n_name
*/