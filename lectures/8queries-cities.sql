SELECT county
FROM Cities_Population;

SELECT count(county)
FROM Cities_Population;


SELECT DISTINCT county
FROM Cities_Population;

SELECT count(DISTINCT county)
FROM Cities_Population;


select count(*) as cnt,
    min(pop_2010) as min_pop,
    avg(pop_2010) as avg_pop,
    max(pop_2010) as max_pop
from Cities_Population;

select max(pop_2010-pop_2000) as max_pop_increase,
    min(pop_2010-pop_2000) as max_pop_decrease,
    avg(pop_2010-pop_2000) as avg_pop_increase
from Cities_Population;


select county,
    count(*) as no_city,
    min(pop_2010) as min_pop,
    avg(pop_2010) as avg_pop,
    max(pop_2010) as max_pop,
    sum(pop_2010) as total_pop
from Cities_Population
group by county;

select county,
    count(*) as no_city,
    min(pop_2010) as min_pop,
    avg(pop_2010) as avg_pop,
    max(pop_2010) as max_pop,
    sum(pop_2010) as total_pop
from Cities_Population
group by county
order by total_pop desc;

select county,
    count(*) as no_city,
    min(pop_2010) as min_pop,
    avg(pop_2010) as avg_pop,
    max(pop_2010) as max_pop,
    sum(pop_2010) as total_pop
from Cities_Population
group by county
having no_city >= 10
order by no_city desc, total_pop desc;


select county,
    sum(pop_2000-pop_1990) as change_2000_1990,
    sum(pop_2010-pop_2000) as change_2010_2000
from Cities_Population
group by county
order by change_2010_2000 desc;

select county,
    sum(pop_2000-pop_1990) as change_2000_1990,
    sum(pop_2010-pop_2000) as change_2010_2000
from Cities_Population
group by county
having change_2010_2000 > change_2000_1990
order by change_2010_2000 desc;
