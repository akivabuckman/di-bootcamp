set datestyle to 'dmy'; -- because dates are given in this format
-- insert into students (first_name, last_name, birth_date)
-- values
-- ('Marc', 'Benichou', '02/11/1998'),
-- ('Yoan', 'Cohen', '03/12/2010'),
-- ('Lea', 'Benichou', '27/07/1987'),
-- ('Amelia', 'Dux', '07/04/1996'),
-- ('David', 'Grez', '14/06/2003'),
-- ('Omer', 'Simpson', '03/10/1980');
-- insert into students (last_name, first_name, birth_date)
-- values ('Buckman', 'Akiva', '02/05/1991');

select * from students;

select first_name, last_name from students;

select first_name, last_name from students where id = 2;

select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc';

select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc';

select first_name, last_name from students where first_name ilike '%a%';

select first_name, last_name from students where first_name ilike 'a%';

select first_name, last_name from students where first_name ilike '%a_';

select first_name, last_name from students where id = 1 and id = 3; -- the exercise says AND, which is impossible for an entry so returns empty table

select * from students where birth_date >= '01/01/2000';

