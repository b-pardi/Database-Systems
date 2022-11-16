-- SQLite

drop view PC_Maker;
drop view Laptop_Maker;
drop view Printer_Maker;
drop view Product_Price;


create view PC_Maker(model, speed, ram, hd, price, maker) as
    select PC.model, speed, ram, hd, price, maker
    from PC, Product P
    where PC.model = P.model;

create view Laptop_Maker(model, speed, ram, hd, screen, price, maker) as
    select L.model, speed, ram, hd, screen, price, maker
    from Laptop L, Product P
    where L.model = P.model;

create view Printer_Maker(model, color, type, price, maker) as
    select Pr.model, Pr.color, Pr.type, price, maker
    from Printer Pr, Product P
    where Pr.model = P.model;

create view Product_Price(model, type, maker, price) as
    select P.model, P.type, maker, price
    from Product P, PC
    where P.model = PC.model
    UNION
    select P.model, P.type, maker, price
    from Product P, Laptop L
    where P.model = L.model
    UNION
    select P.model, P.type, maker, price
    from Product P, Printer Pr
    where P.model = Pr.model;


select *
from PC_Maker;

select *
from Laptop_Maker;

select *
from Printer_Maker;

select *
from Product_Price;

--2
select distinct maker
from product p, Printer pr
where p.model = pr.model
    and color = true
    and price < 200;

select distinct maker
from Printer_Maker
where color = true
    and price < 200;

--3
select maker
from product
where type = 'pc'
intersect
select maker
from product
where type = 'laptop'
intersect
select maker
from product
where type = 'printer';

select maker
from PC_Maker
intersect
select maker
from Laptop_Maker
intersect
select maker
from Printer_Maker;

--5
select P1.maker, P1.model, P2.model, (PC.price+L.price) as cPrice
from product p1, product p2, PC, Laptop L
where P1.model = PC.model
    and P2.model = L.model
    and P1.maker = P2.maker
    and cPrice = 
        (select min(pc1.price+L1.price)
        from product p11, product p21, PC pc1, Laptop L1
        where P11.model = pc1.model
            and P21.model = L1.model
            and P11.maker = P21.maker
            and p11.maker = P1.maker);

select P.maker, P.model, L.model, (P.price+L.price) as cPrice
from PC_Maker P, Laptop_Maker L
where P.maker = L.maker
    and cPrice = 
        (select min(P1.price+L1.price)
        from PC_Maker P1, Laptop_Maker L1
        where P1.maker = L1.maker
            and P.maker = P1.maker);

--9
select count(*)
from
    (select maker, count(*) as cnt
    from
        (select maker, pr.type, count(*)
        from Product P, Printer pr
        where P.model = pr.model
        group by maker, pr.type) SQ1
    group by SQ1.maker
    having cnt >= 2) SQ2;

select count(*)
from
    (select maker, count(*) as cnt
    from
        (select maker, type, count(*)
        from Printer_Maker
        group by maker, type) SQ1
    group by SQ1.maker
    having cnt >= 2) SQ2;

--14
select pr.model, pr.price
from Product p1, Printer pr, Product p2, PC
where p1.model = pr.model
    and p2.model = PC.model
    and p1.maker = p2.maker
    and PC.price =
        (select max(price)
        from Product p, PC
        where p.model = PC.model
            and p.maker in
                (select maker
                from Product
                where type = 'pc'
                intersect
                select maker
                from Product
                where type = 'printer'))
    and pr.price = 
        (select min(pr.price)
        from Product p1, Printer pr, Product p2, PC
        where p1.model = pr.model
            and p2.model = PC.model
            and p1.maker = p2.maker
            and PC.price =
                (select max(price)
                from Product p, PC
                where p.model = PC.model
                    and p.maker in
                        (select maker
                        from Product
                        where type = 'pc'
                        intersect
                        select maker
                        from Product
                        where type = 'printer')));

select P.model, P.price
from Printer_Maker P, PC_Maker PC
where P.maker = PC.maker
    and PC.price =
        (select max(price)
        from PC_Maker
        where maker in
                (select maker
                from Printer_Maker
                intersect
                select maker
                from PC_Maker))
    and P.price = 
        (select min(P1.price)
        from Printer_Maker P1, PC_Maker PC1
        where P1.maker = PC1.maker
            and PC1.price =
                    (select max(price)
                    from PC_Maker
                    where maker in
                            (select maker
                            from PC_Maker
                            intersect
                            select maker
                            from Printer_maker)));

--15
select S1.maker, avgPC, avgL, avgPrint
from
    (select maker, avg(price) as avgPC
    from Product p, PC
    where p.model = PC.model
        and maker in
            (select maker
            from Product
            where type = 'pc'
            intersect
            select maker
            from Product
            where type = 'laptop'
            intersect
            select maker
            from Product
            where type = 'printer')
    group by maker) S1,
    (select maker, avg(price) as avgL
    from Product p, Laptop l
    where p.model = l.model
        and maker in
            (select maker
            from Product
            where type = 'pc'
            intersect
            select maker
            from Product
            where type = 'laptop'
            intersect
            select maker
            from Product
            where type = 'printer')
    group by maker) S2,
    (select maker, avg(price) as avgPrint
    from Product p, Printer pr
    where p.model = pr.model
        and maker in
            (select maker
            from Product
            where type = 'pc'
            intersect
            select maker
            from Product
            where type = 'laptop'
            intersect
            select maker
            from Product
            where type = 'printer')
    group by maker) S3
where S1.maker = S2.maker
    and S2.maker = S3.maker;

select S1.maker, avgPC, avgL, avgPrint
from
    (select maker, avg(price) as avgPC
    from PC_Maker
    group by maker) S1,
    (select maker, avg(price) as avgL
    from Laptop_Maker
    group by maker) S2,
    (select maker, avg(price) as avgPrint
    from Printer_Maker
    group by maker) S3
where S1.maker = S2.maker
    and S2.maker = S3.maker;

--16
select maker
from
    (select maker, count(*) as cnt
    from Laptop l, Product p
    where l.model = p.model
    group by maker
    having cnt = 1) S;

select maker
from
    (select maker, count(*) as cnt
    from Laptop_Maker
    group by maker
    having cnt = 1) S;

--18
select maker
from
    (select maker, count(*) as cnt
    from Laptop l, Product p
    where l.model = p.model
    group by maker
    having cnt = 1)
intersect
select maker
from
    (select maker, count(*) as cnt
    from PC, Product p
    where PC.model = p.model
    group by maker
    having cnt = 3);

select maker
from
    (select maker, count(*) as cnt
    from Laptop_Maker
    group by maker
    having cnt = 1)
intersect
select maker
from
    (select maker, count(*) as cnt
    from PC_Maker
    group by maker
    having cnt = 3);

--20
select L.model, L.screen, L.speed, P.maker
from Product P, Laptop L
where P.model = L.model
    and L.screen >=15
    and L.speed < 2
    and P.maker in
        (select maker
    from Product
    where type = 'printer');

select model, screen, speed, maker
from Laptop_Maker
where screen >=15
    and speed < 2
    and maker in
        (select maker
        from Printer_Maker);


drop view Prod_Printer;
CREATE VIEW Prod_Printer(model, maker, type) AS
    SELECT model, maker, type
    FROM Product
    WHERE type = 'printer';

insert into Prod_Printer(model, maker, type)
values(3108, 'A', 'printer');


drop table Printer_Maker_M;
CREATE TABLE Printer_Maker_M(
    model integer,
    color bool,
    type varchar(30),
    price decimal(7,2),
    maker char(32)
);

delete from Printer_Maker_M;
INSERT INTO Printer_Maker_M
    SELECT Pr.model, Pr.color, Pr.type, price, maker
    from Printer Pr, Product P
    where Pr.model = P.model;


INSERT INTO Product(model, type, maker)
VALUES(3108, 'printer', 'A');
INSERT INTO Printer(model, color, type, price)
VALUES(3108, false, 'laser', 169);
INSERT INTO Printer_Maker_M
    SELECT Pr.model, Pr.color, Pr.type, price, maker
    from Printer Pr, Product P
    where Pr.model = P.model AND P.model = 3108;


UPDATE Product
SET maker = 'A'
WHERE maker = 'D' and type = 'printer';
UPDATE Printer_Maker_M
SET maker = 'A'
WHERE maker = 'D';
