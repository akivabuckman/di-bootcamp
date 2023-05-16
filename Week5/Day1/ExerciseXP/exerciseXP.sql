-- insert into items (item_name, item_price)
-- values ('Small Desk', 100), ('Large Desk', 300), ('Fan', 80);

-- insert into customerss (first_name, last_name)
-- values ('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

select * from items;

select * from items where item_price > 80;

select * from items where item_price < 300;

select * from customerss where last_name = 'Smith'; --will return an empty table

select * from customerss where last_name = 'Jones';

select * from customerss where last_name != 'Scott';