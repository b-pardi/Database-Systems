-- ALL
select 'ALL' as distributor_type, 'ALL' as product_type, count(distributor.model) as num_prod, sum(distributor.price) as tot_price
from distributor

union

select
    -- determine distributor
    CASE
        when 1
        then 
            'ALL'
    end distributor_type,
    -- determine product type
    CASE
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'laptop')
        THEN
            'laptop'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'pc')
        THEN
            'pc'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'printer')
        THEN
            'printer'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and (product.type = 'printer'
                or product.type = 'laptop'
                or product.type = 'pc'))
        THEN
            'ALL'
        end product_type,
    
    -- count appropriately
    count(distributor.model) as num_prod,

    -- sum appropriately
    sum(distributor.price) as tot_price

from distributor
group by distributor_type, product_type

union

-- distributors
select 'distributor' as distributor_type, 'ALL' as product_type, count(distributor.model) as num_prod, sum(distributor.price) as tot_price
from distributor
where distributor.name not in (select product.maker from product)

union

select
    -- determine distributor
    CASE
        when distributor.name not in
            (select product.maker from product)
        then 
            'distributor'
    end distributor_type,
    
    -- determine product type
    CASE
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'laptop')
        THEN
            'laptop'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'pc')
        THEN
            'pc'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'printer')
        THEN
            'printer'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and (product.type = 'printer'
                or product.type = 'laptop'
                or product.type = 'pc'))
        THEN
            'ALL'
        end product_type,
    
    -- count appropriately
    CASE
        when distributor.name not in
            (select product.maker from product)
        then count(distributor.model)
    end num_prod,

    -- sum appropriately
    CASE
        when distributor.name not in
            (select product.maker from product)
        then sum(distributor.price)
    end tot_price

from distributor

where distributor.name not in (select product.maker from product)

group by distributor_type, product_type

union

-- producer
select 'producer' as distributor_type, 'ALL' as product_type, count(distributor.model) as num_prod, sum(distributor.price) as tot_price
from distributor
where distributor.name in (select product.maker from product)

union

SELECT
    CASE
    when distributor.name in
            (select product.maker from product)
        then 
            'producer'
    end distributor_type,
    -- determine product type
    CASE
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'laptop')
        THEN
            'laptop'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'pc')
        THEN
            'pc'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and product.type = 'printer')
        THEN
            'printer'
        when distributor.model IN
            (select product.model
            from product, distributor
            where product.model = distributor.model
            and (product.type = 'printer'
                or product.type = 'laptop'
                or product.type = 'pc'))
        THEN
            'ALL'
        end product_type,
    
    -- count appropriately
    CASE
        when distributor.name in
            (select product.maker from product)
        then count(distributor.model)
    end num_prod,

    -- sum appropriately
    CASE
        when distributor.name in
            (select product.maker from product)
        then sum(distributor.price)
    end tot_price

from distributor
where distributor.name in (select product.maker from product)
group by distributor_type, product_type
