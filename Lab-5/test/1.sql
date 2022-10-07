-- How many customers are not from EUROPE or AFRICA or ASIA?

SELECT COUNT(customer.c_custkey)

FROM customer,
nation,
region

WHERE c_nationkey = n_nationkey
AND n_regionkey = r_regionkey

AND r_name NOT IN ('EUROPE', 'ASIA', 'AFRICA')