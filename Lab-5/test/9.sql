-- Print the name of the parts supplied by suppliers from UNITED STATES that have total value in the top
-- 1% total values across all the supplied parts. The total value is ps supplycost*ps availqty. Hint:
-- Use the LIMIT keyword

SELECT p_name
FROM (SELECT p_name, ps_supplycost*ps_availqty as total_val1
    FROM partsupp, part, nation, supplier
    WHERE p_partkey = ps_partkey
    AND ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES'

    AND total_val1 IN (SELECT ps_supplycost*ps_availqty as total_val2
        FROM partsupp
        ORDER BY total_val2 DESC
        LIMIT (SELECT 0.01 * COUNT(*) FROM partsupp) )
    ORDER BY total_val1 DESC    
    )
/*
LIMIT (SELECT COUNT(p_name) as p_count
    FROM partsupp, part, nation, supplier
    WHERE p_partkey = ps_partkey
    AND ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND n_name = 'UNITED STATES') / 100
*/
/*
SELECT p_name
FROM part, nation, supplier, partsupp, 
    (SELECT p_name as total_pname,
    ps_supplycost*ps_availqty as total_val,
    ps_partkey as total_partkey,
    ps_suppkey as total_supkey
    FROM partsupp, part
    WHERE p_partkey = ps_partkey
    ORDER BY total_val DESC
    )

WHERE p_partkey = total_partkey
AND total_supkey = s_suppkey
AND s_nationkey = n_nationkey
AND n_name = 'UNITED STATES'
*/