-- Find how many parts are supplied by exactly two suppliers from UNITED STATES

SELECT COUNT(sq_parts.p_partkey)
FROM (SELECT p_partkey
    FROM supplier, partsupp, part, nation
    WHERE s_suppkey = ps_suppkey
    AND p_partkey = ps_partkey
    AND s_nationkey = n_nationkey

    AND n_name = 'UNITED STATES'
    GROUP BY p_partkey
    HAVING COUNT(p_partkey) = 2) as sq_parts
