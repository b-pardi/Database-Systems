-- SQLite

select maker
from product;

select distinct maker
from product;

select maker, type
from product;

select distinct maker, type
from product;


select count(*)
from product
where maker = 'A';

select AVG(price)
from PC;

select MIN(price) as min_price, AVG(price) as avg_price, MAX(price) as max_price
from laptop;

select min(speed), min(hd)
from pc
where price > 1000;


select count (*)
from product
where type = 'pc';

select count (maker)
from product
where type = 'pc';

select count (distinct maker)
from product
where type = 'pc';


--6.4.6 a)
select avg(speed) as avg_speed
from pc;

--6.4.6 b)
select avg(speed) as avg_speed
from laptop
where price > 1000;

--6.4.6 e)
select speed, avg(price) as avg_price
from pc
group by speed;

--6.4.6 i)
select speed, avg(price) as avg_price
from pc
where speed > 2
group by speed;

--6.4.6 g)
select maker, count (distinct model)
from product
group by maker;

select maker, count (distinct model)
from product
where type = 'pc'
group by maker;

select maker, count (distinct model) as models
from product
where type = 'pc'
group by maker
having models >= 3;
