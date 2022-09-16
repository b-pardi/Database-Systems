-- Find the number of customers that received a discount of at least 7% for one of the line items on their
-- orders. Count every customer exactly once even if they have multiple discounted line item
SELECT COUNT(DISTINCT customer.c_name)
FROM customer
JOIN orders
ON orders.o_custkey = customer.c_custkey
JOIN lineitem
ON orders.o_orderkey = lineitem.l_orderkey
WHERE lineitem.l_discount >= 0.07