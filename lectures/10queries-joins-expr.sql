-- SQLite

select *
from Product, PC;

select *
from Product cross join PC;


select *
from Product P, PC
where P.model = PC.model;

select *
from Product P join PC
        on P.model = PC.model;

select *
from Product P inner join PC
    on P.model = PC.model;

select *
from Product P natural join PC;

select *
from Product natural join Printer;


select P1.maker, P1.model, P2.model
from Product P1, Product P2
where P1.maker = P2.maker and
    P1.type = 'pc' and
    P2.type = 'laptop';

select P1.maker, P1.model, P2.model
from Product P1 join Product P2
    on P1.maker = P2.maker
where
    P1.type = 'pc' and
    P2.type = 'laptop';


select PC1.model as model_1, PC2.model as model_2
from PC PC1, PC PC2
where PC1.speed = PC2.speed AND
    PC1.ram = PC2.ram and
    PC1.model < PC2.model;

select PC1.model as model_1, PC2.model as model_2
from PC PC1 join PC PC2
    on PC1.speed = PC2.speed AND
    PC1.ram = PC2.ram and
    PC1.model < PC2.model;

select PC1.model as model_1, PC2.model as model_2
from PC PC1 join PC PC2
    on PC1.speed = PC2.speed AND
        PC1.ram = PC2.ram
where PC1.model < PC2.model;

select PC1.model as model_1, PC2.model as model_2
from PC PC1 inner join PC PC2
    on PC1.speed = PC2.speed AND
        PC1.ram = PC2.ram and
        PC1.model < PC2.model;

select PC1.model as model_1, PC2.model as model_2
from PC PC1 inner join PC PC2
    on PC1.speed = PC2.speed AND
        PC1.ram = PC2.ram
where PC1.model < PC2.model;


select *
from Product P left outer join PC
    on P.model = PC.model
where P.type = 'pc';

select *
from Product P left outer join PC
    on P.model = PC.model;

select *
from Product P natural left outer join PC;

select *
from Product P natural left outer join PC
where P.type = 'pc';


--2.4.1 a)
select model
from PC
where speed >= 3;


--2.4.1 b)
select maker
from Product P, Laptop L
where P.model = L.model and
    hd >= 100;


--2.4.1 d)
select model
from Printer
where color = true and type = 'laser';


--2.4.1 i)
select distinct maker
from Product
where model in 
    (select model
    from 
        (select model, speed
        from PC
        UNION
        select model, speed
        from Laptop) FM
    where speed = (select max(speed)
                from
                    (select speed
                    from PC
                    UNION
                    select speed
                    from Laptop)));


--2.4.1 j)
select P1.maker
from Product P1, Product P2, Product P3,
    PC PC1, PC PC2, PC PC3
WHERE
    P1.maker = P2.maker AND
    P2.maker = P3.maker AND
    P1.model = PC1.model AND
    P2.model = PC2.model AND
    P3.model = PC3.model AND
    PC1.speed < PC2.speed AND
    PC2.speed < PC3.speed;

select distinct P1.maker
from Product P1, Product P2, Product P3,
    PC PC1, PC PC2, PC PC3
WHERE
    P1.maker = P2.maker AND
    P2.maker = P3.maker AND
    P1.model = PC1.model AND
    P2.model = PC2.model AND
    P3.model = PC3.model AND
    PC1.speed < PC2.speed AND
    PC2.speed < PC3.speed;

select *
from Product P, PC
where P.model = PC.model;


--2.4.1 k)
select maker, count(*) as pc_no
from Product
where type = 'pc'
group by maker
having pc_no = 3;

select maker
from
    (select maker, count(*) as pc_no
    from Product
    where type = 'pc'
    group by maker
    having pc_no = 3);
