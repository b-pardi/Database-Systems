-- SQLite

--6.1.3 a)
select model, speed, hd
from pc
where price < 1000;

--6.1.3 b)
select model, speed as gigahertz, hd as gigabytes
from pc
where price < 1000;

--6.1.3 c)
select maker
from product
where type = 'printer';

select distinct maker
from product
where type = 'printer';

--6.1.3 d)
select model, ram, screen
from laptop
where price > 1500;

--6.1.3 e)
select *
from printer
where color = true;

--6.1.3 f)
select model, hd
from pc
where speed = 3.2 and price < 2000;
