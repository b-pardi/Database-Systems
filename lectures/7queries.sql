-- SQLite

select distinct maker
from product
where type = 'pc';

select maker
from product
where type = 'pc';

select maker
from product
where type = 'laptop';

select maker
from product
where type = 'pc'
union
select maker
from product
where type = 'laptop';


select maker
from product
where type = 'pc'
union all
select maker
from product
where type = 'laptop';

select maker
from product
where type = 'pc' or type = 'laptop';


select maker
from product
where type = 'pc'
intersect
select maker
from product
where type = 'laptop';

select maker
from product
where type = 'pc' and type = 'laptop';


select maker
from product
where type = 'pc'
except
select maker
from product
where type = 'laptop';

select maker
from product
where type = 'laptop'
except
select maker
from product
where type = 'pc';

select maker
from product
where type = 'laptop' and type <> 'pc';


select model, (speed+ram+hd)/price as score
from pc
union
select model, (speed+ram+hd+screen)/price as score
from laptop
order by score desc;

select model, speed, price
from pc
union
select model, speed, ram
from laptop
order by score desc;
