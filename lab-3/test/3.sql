-- Find all the line items with the return flag set to R on the receipt date of September 9, 1993. Print
--l receiptdate, l returnflag, l extendedprice, and l tax for every line item
SELECT l_receiptdate, l_returnflag, l_extendedprice, l_tax
FROM lineitem
WHERE l_returnflag = 'R'
AND l_receiptdate = '1993-09-09';