CREATE TRIGGER t1 AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE orders
    SET o_orderdate = '2021-12-01'
    WHERE o_orderkey = NEW.o_orderkey;
END;

INSERT INTO orders 
SELECT *
FROM orders
WHERE o_orderdate LIKE '1996-12%';

SELECT COUNT(DISTINCT o_orderkey) FROM orders
WHERE o_orderdate LIKE '2021-%';