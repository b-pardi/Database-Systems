CREATE TRIGGER t3 AFTER UPDATE ON customer
FOR EACH ROW

WHEN
    new.c_acctbal > 0

BEGIN
    UPDATE customer
    set c_comment = 'Positive balance'
    WHERE c_custkey = new.c_custkey;

END;

UPDATE customer
SET c_acctbal = 100
WHERE c_nationkey IN (
    SELECT c_nationkey
    FROM customer, nation
    
    WHERE n_nationkey = c_nationkey
    AND n_name = 'UNITED STATES'
);

SELECT COUNT(c_custkey) FROM customer, nation, region
WHERE n_nationkey = c_nationkey
AND n_regionkey = r_regionkey
AND r_name = 'AMERICA'
AND c_acctbal < 0;