-- What is the total account balance among the customers in every market segment?
SELECT c_mktsegment, SUM(c_acctbal)
FROM customer
GROUP BY c_mktsegment;