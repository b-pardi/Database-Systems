--select result column, from table, where search column...
--What is the account balance, phone number, and address of Customer#000000020?
SELECT c_acctbal, c_phone, c_address
FROM customer
WHERE c_name = 'Customer#000000020';