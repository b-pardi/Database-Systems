select *
from Cities_Population;

SELECT city
FROM Cities_Population;

SELECT city, county
FROM Cities_Population;

SELECT
    city,
    county,
    incorporated AS established,
    pop_2010 AS current_population
FROM Cities_Population;

SELECT
    city,
    pop_2010 - pop_2000 AS pop_increase
FROM Cities_Population;


select *
from Cities_Population
where county = 'Merced';

SELECT city, county, pop_2000, pop_2010
FROM Cities_Population
WHERE (county = 'Merced' OR county = 'Stanislaus') AND
    pop_2010 > pop_2000;


SELECT city
FROM Cities_Population
WHERE city LIKE 'San %';

SELECT city
FROM Cities_Population
WHERE city LIKE 'San%';

SELECT city
FROM Cities_Population
WHERE city LIKE '%San__ %';

SELECT city
FROM Cities_Population
WHERE city LIKE '%San__%';


SELECT city
FROM Cities_Population
WHERE pop_1980 IS NULL;

update Cities_Population
set pop_1980 = NULL
where incorporated >= 1980;


SELECT city, incorporated, pop_1980, pop_1990
FROM Cities_Population
WHERE county = 'Los Angeles' and pop_1980 is null;

SELECT city,
    pop_1990 - pop_1980 as change_1980_1990
FROM Cities_Population
WHERE county = 'Los Angeles';

SELECT city,
    case pop_1980 is null
        when true then pop_1990
        else pop_1990 - pop_1980
    end as change_1980_1990
FROM Cities_Population
WHERE county = 'Los Angeles';


SELECT
    city,
    pop_2010
FROM Cities_Population
ORDER BY
    pop_2010;

SELECT
    city,
    pop_2010
FROM Cities_Population
ORDER BY
    pop_2010 desc;

SELECT
    city,
    pop_2010 - pop_2000 as change_2000_2010
FROM Cities_Population
ORDER BY
    change_2000_2010;

SELECT
    city,
    pop_2010 - pop_2000 as change_2000_2010
FROM Cities_Population
ORDER BY
    change_2000_2010 desc;

select county, city
from Cities_Population
order by county, city;
