-- Continuation of the Exercise XP

-- Select
-- For the following questions, you have to fetch the first_names, last_names and birth_dates of the students.

-- Fetch the first four students. You have to order the four students alphabetically by last_name.
-- Fetch the details of the youngest student.
-- Fetch three students skipping the first two students.

select first_name, last_name, birth_date from students order by last_name asc limit 4;

select first_name, last_name, birth_date from students where birth_date = (select min(birth_date) from students);

select first_name, last_name, birth_date from students offset 2 limit 3;