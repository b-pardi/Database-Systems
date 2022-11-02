-- for each supplier, find 2 nations with largest number
-- of lineitems supplied by supplier
-- that are ordered by customers from that nation

-- for each s in supplier
--      for each n in nation
--          count(s,n)

select s_name, n_name, count(l_quantity) as ct
        from supplier, nation, customer, lineitem, orders
        where s_suppkey = l_suppkey
        and l_orderkey = o_orderkey
        and o_custkey = c_custkey
        and c_nationkey = n_nationkey
        
        group by s_name, n_name
        order by s_name, ct desc
        --and s_name = 'Supplier#000000001'
        --and n_name = 'UNITED STATES'



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