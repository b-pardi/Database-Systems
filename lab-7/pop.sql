-- for each supplier, find 2 nations with largest number
-- of lineitems supplied by supplier
-- that are ordered by customers from that nation


-- for each s in supplier
--      for each n in nation
--          count(s,n)

select s_name, n_name, ct, max(cap)
    from(select s_name, n_name, count(l_quantity) as ct, sum(p_size) * 2 as cap
    from supplier, nation, customer, lineitem, orders, part
    where s_suppkey = l_suppkey
    and l_orderkey = o_orderkey
    and o_custkey = c_custkey
    and c_nationkey = n_nationkey
    and l_partkey = p_partkey

    group by s_name, n_name
    order by s_name, ct desc)
group by s_name

