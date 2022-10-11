-- Find the nation(s) with the smallest number of customers

SELECT n_name
FROM (SELECT n_name, MIN(cust_cnt)
    FROM (SELECT n_name, COUNT(c_custkey) as cust_cnt
        FROM customer, nation
        WHERE c_nationkey = n_nationkey
        GROUP BY n_name
    )
)