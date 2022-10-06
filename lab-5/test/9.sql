-- Print the name of the parts supplied by suppliers from UNITED STATES that have total value in the top
-- 1% total values across all the supplied parts. The total value is ps supplycost*ps availqty. Hint:
-- Use the LIMIT keyword

SELECT p_name
FROM part, (SELECT p_name as total_pname,
    ps_supplycost*ps_availqty as total_val
    FROM partsupp, part, nation, supplier
    WHERE p_partkey = ps_partkey
    AND ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'
    ORDER BY total_val DESC ) total_tbl

WHERE p_name = total_pname
LIMIT (SELECT COUNT(p_name) as p_count
    FROM partsupp, part, nation, supplier
    WHERE p_partkey = ps_partkey
    AND ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES') / 100