CREATE TRIGGER t2 AFTER UPDATE ON customer
FOR EACH ROW

WHEN
    new.c_acctbal < 0

BEGIN
    UPDATE customer
    set c_comment = 'Negative balance!!!'
    WHERE c_custkey = new.c_custkey;

END;

UPDATE customer
SET c_acctbal = -100
WHERE c_nationkey IN (
    SELECT c_nationkey
    FROM customer, nation, region
    
    WHERE r_regionkey = n_regionkey
    AND n_nationkey = c_nationkey
    AND r_name = 'AMERICA'
);

SELECT COUNT(c_custkey) FROM customer, nation
WHERE n_nationkey = c_nationkey
AND n_name = 'CANADA'
AND c_acctbal < 0;