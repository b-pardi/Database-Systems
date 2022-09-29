-- SQLite

select *
from PC
where price =
    (select max(price) from PC);


select maker
from Product
where model in
    (select model
    from PC
    where price =
        (select max(price) from PC)
    );

select maker
from Product
where type = 'pc' and
    maker IN (select maker
                from Product
                where type = 'laptop');

select maker
from Product
where type = 'pc' and
    maker not in (select maker
    from Product
    where type = 'laptop');


select *
from PC
where not EXISTS
    (select *
    from PC PC1
    where PC1.price > PC.price
    );


select P.model, maker, SQ.price
FROM Product P,
    (select model, price
    from PC
    where ram = (select max(ram) from PC)
    ) SQ
where P.model = SQ.model;


select maker, ram
FROM Product P, PC
where P.model = PC.model
order by ram DESC
limit 1;

select maker, ram
FROM Product P, PC
where P.model = PC.model AND
    not exists (select ram
                from PC PC1
                where PC1.ram > PC.ram);


--6.3.1 a)
select maker
from Product
where model in (select model
                from PC
                where speed >= 3);


--6.3.1 b)
select *
from Printer
where price = (select max(price)
                from Printer);

select *
from Printer P
where not exists (select *
                    from Printer Pp
                    where Pp.price > P.price);


--6.3.1 c)
select *
from Laptop L
where exists (select *
                from PC
                where PC.speed > L.speed);

select *
from Laptop L
where not exists (select *
                  from PC
                  where PC.speed < L.speed);


--6.3.1 d)
select model
from
    (select model, price
    from PC
    where not exists (select *
                        from PC pc1
                        where pc1.price > PC.price)

    UNION

    select model, price
    from Laptop L
    where not exists (select *
                        from Laptop L1
                        where L1.price > L.price)

    UNION

    select model, price
    from Printer P
    where not exists (select *
                        from Printer P1
                        where P1.price > P.price)
    ) SQ
where not exists 
    (select *
    from 
        (select price from PC
        UNION
        select price from Laptop
        UNION
        select price from Printer) SQ1
    where SQ1.price > SQ.price
    );


--6.3.1 e)
select maker
from Product P,
    (select Pr.model
    from Printer Pr
    where Pr.color = true AND
        not exists (select *
                    from Printer Pr1
                    where Pr1.color = true AND
                        Pr1.price > Pr.price)
    ) SQ
where P.model = SQ.model;


--6.3.1 f)
select maker
from Product P,
    (select SQ.model
    from
        (select PC.model, PC.speed
        from PC
        where PC.ram = (select min(ram)
                        from PC)
        ) SQ
    where not exists 
        (select *
         from
            (select PC1.speed
                from PC PC1
                where PC1.ram = (select min(ram)
                                from PC)
            ) SQ1
        where SQ1.speed > SQ.speed
        )
    ) SQ3    
where P.model = SQ3.model;
