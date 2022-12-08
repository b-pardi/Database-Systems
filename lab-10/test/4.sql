CREATE TRIGGER t4_1 AFTER INSERT ON lineitem
FOR EACH ROW

BEGIN
    UPDATE orders
    SET o_orderpriority = 'HIGH'
    WHERE o_orderkey = new.l_orderkey;
END;

CREATE TRIGGER t4_2 AFTER DELETE ON lineitem
FOR EACH ROW

BEGIN
    UPDATE orders
    SET o_orderpriority = 'HIGH'
    WHERE o_orderkey = old.l_orderkey;
END;

DELETE FROM lineitem
WHERE l_orderkey IN (
    SELECT o_orderkey
    FROM lineitem, orders
    WHERE l_orderkey = o_orderkey
    AND o_orderdate LIKE '1995-12%'
);

SELECT COUNT(o_orderkey)
FROM orders
WHERE o_orderdate BETWEEN '1995-10-01' AND '1995-12-31'
AND o_orderpriority = 'HIGH';