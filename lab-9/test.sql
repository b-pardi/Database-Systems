-- V1
create view V1(c_custkey, c_name, c_address, c_phone, c_acctbal,
c_mktsegment, c_comment, c_nation, c_region) as 
    select c_custkey, c_name, c_address, c_phone, c_acctbal,
    c_mktsegment, c_comment, n_name, r_name
    from customer, nation, region
    where c_nationkey = n_nationkey
    and n_regionkey = r_regionkey;

-- V2
create view V2(s_suppkey, s_name, s_address, s_phone,
s_acctbal, s_comment, s_nation, s_region) as
    select s_suppkey, s_name, s_address, s_phone,
    s_acctbal, s_comment, n_name, r_name
    from supplier, nation, region
    where s_nationkey = n_nationkey
    and n_regionkey = r_regionkey;

-- V5
create view V5(o_orderkey, o_custkey, o_orderstatus, o_totalprice,
o_orderyear, o_orderpriority, o_clerk, o_shippriority, o_comment) AS
    select o_orderkey, o_custkey, o_orderstatus, o_totalprice,
    substr(o_orderdate, 1, 4), o_orderpriority, o_clerk, o_shippriority, o_comment
    from orders;

-- V10
create view V10(p_type, min_discount, max_discount) AS
    select p_type, min(l_discount), max(l_discount)
    from lineitem, part
    where l_partkey = p_partkey
    group by p_type;

-- V151
create view V151(c_custkey, c_name, c_nationkey, c_acctbal) as
    select c_custkey, c_name, c_nationkey, c_acctbal
    from customer
    where c_acctbal > 0;

-- V152
create view V152(s_suppkey, s_name, s_nationkey, s_acctbal) as
    select s_suppkey, s_name, s_nationkey, s_acctbal
    from supplier
    where s_acctbal < 0;

-- Q1
select c_name, sum(o_totalprice)
from V1, orders
where o_custkey = c_custkey
and c_nation = "FRANCE"
and o_orderdate LIKE '1995%'
group by c_name;

-- Q2
select s_region, count(*)
from V2
group by s_region;

-- Q3
select c_nation, count(*)
from orders, V1
where c_custkey = o_custkey
and c_region = 'AMERICA'
group by c_nation;

-- Q4
select s_name, count(ps_partkey)
from partsupp, V2, part
where p_partkey = ps_partkey
and ps_suppkey = s_suppkey
and s_nation = 'CANADA'
and p_size < 20
group by s_name;

-- Q5
select c_name, count(*)
from V5, V1
where o_custkey = c_custkey
and c_nation = 'GERMANY'
and o_orderyear = '1993'
group by c_name;

-- Q6
select s_name, o_orderpriority, count(distinct ps_partkey)
from V5, partsupp, lineitem, V2
where l_orderkey = o_orderkey
and l_partkey = ps_partkey
and l_suppkey = ps_suppkey
and ps_suppkey = s_suppkey
and s_nation = 'CANADA'
group by s_name, o_orderpriority;

-- Q7
select c_nation, o_orderstatus, count(*)
from V1, V5
where o_custkey = c_custkey
and c_region = 'AMERICA'
group by c_nation, o_orderstatus;

-- Q8
select s_nation, count(distinct l_orderkey) as co
from V2, V5, lineitem
where o_orderkey = l_orderkey
and l_suppkey = s_suppkey
and o_orderstatus = 'F'
and o_orderyear = '1995'
group by s_nation
having co > 50;

-- Q9
select count(distinct o_clerk)
from V5, V2, lineitem
where o_orderkey = l_orderkey
and l_suppkey = s_suppkey
and s_nation = 'UNITED STATES';

-- Q10
select p_type, min_discount, max_discount
from V10
where p_type like '%ECONOMY%'
and p_type like '%COPPER%'
group by p_type;

-- Q11
select s1.s_region, s1.s_name, s1.s_acctbal
from V2 s1
where s1.s_acctbal = (select max(s2.s_acctbal) 
                from V2 s2
                where s1.s_region = s2.s_region
                )
order by s_region;

-- Q12
select s_nation, max(s_acctbal) as mb
from V2
group by s_nation
having mb > 9000;

-- Q13
select count(*)
from V5, V2, V1, lineitem
where o_orderkey = l_orderkey
and o_custkey = c_custkey
and l_suppkey = s_suppkey
and s_region = 'AFRICA'
and c_nation = 'UNITED STATES';

-- Q14
select s_region, c_region, max(o_totalprice)
from lineitem, V1, V2, V5
where l_suppkey = s_suppkey
and l_orderkey = o_orderkey
and o_custkey = c_custkey
group by s_region, c_region;

-- Q15
select count(distinct l_orderkey)
from lineitem, V152, orders, V151
where l_suppkey = s_suppkey
    and l_orderkey = o_orderkey
    and o_custkey = c_custkey