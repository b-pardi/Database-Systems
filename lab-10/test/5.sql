CREATE TRIGGER t5 AFTER DELETE ON part
FOR EACH ROW

BEGIN
    DELETE FROM partsupp
    WHERE ps_partkey = old.p_partkey;

    DELETE FROM lineitem
    WHERE l_partkey = old.p_partkey;

END;

DELETE FROM part
WHERE p_partkey IN (
    SELECT p_partkey
    FROM part, partsupp, supplier, nation
    WHERE p_partkey = ps_partkey
    AND ps_suppkey = s_suppkey
    AND s_nationkey = n_nationkey
    AND (
        n_name = 'UNITED STATES' OR
        n_name = 'CANADA'
    )
);

SELECT n_name, COUNT(p_partkey)
FROM part, partsupp, supplier, nation, region
WHERE p_partkey = ps_partkey
AND ps_suppkey = s_suppkey
AND s_nationkey = n_nationkey
AND n_regionkey = r_regionkey
AND r_name = 'AMERICA'
GROUP BY n_name;