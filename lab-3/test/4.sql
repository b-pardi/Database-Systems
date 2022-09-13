-- Find the number of line items that have l shipdate equal to l commitdate
SELECT COUNT(*)
FROM lineitem
WHERE l_shipdate = l_commitdate