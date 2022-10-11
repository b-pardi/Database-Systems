-- Find how many suppliers from UNITED STATES supply more than 40 different parts

SELECT COUNT(sq_supp.s_suppkey)
FROM (SELECT s_suppkey
    FROM supplier, partsupp, nation
    WHERE ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    
    AND n_name = 'UNITED STATES'
    GROUP BY s_suppkey
    HAVING COUNT(ps_partkey) > 40    
) as sq_supp