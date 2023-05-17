-- In the dvdrental database write a query to select all the columns from the “customer” table.

-- Write a query to display the names (first_name, last_name) using an alias named “full_name”.

-- Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).

-- Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.

-- Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.

-- Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.

-- Write a query to retrieve all movie details where the movie id is either 15 or 150.

-- Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.

-- No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.

-- Write a query which will find the 10 cheapest movies.

-- Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
-- Bonus: Try to not use LIMIT.

-- Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).

-- You need to check your inventory. Write a query to get all the movies which are not in inventory.

-- Write a query to find which city is in which country.

-- Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.


select * from customer limit 0;

select (first_name, last_name) as full_name from customer;

select distinct create_date from customer;

select * from customer order by first_name desc;

select film_id, title, description, release_year, rental_rate from film order by rental_rate asc;

select address, phone from address where district = 'Texas';

select * from film where film_id in (15, 50);

select film_id, title, description, length, rental_rate from film where title = 'Shrek';

select film_id, title, description, length, rental_rate from film where title ilike 'sh%';

select * from film order by rental_rate asc limit 10;

select * from film order by rental_rate asc offset 10 limit 10;

select first_name, last_name, payment.amount, payment.payment_date
from customer
inner join payment
on customer.customer_id = payment.customer_id
order by customer.customer_id;

select film_id, title
from film
where film_id not in (select film_id from inventory);

select city, country.country
from city
inner join country
on city.country_id = country.country_id;


select *
from payment
inner join staff
on payment.staff_id = staff.staff_id;

select staff_id, customer.customer_id, (customer.first_name, customer.last_name) as customer_name, amount, payment_date
from payment
inner join customer
on payment.customer_id = customer.customer_id
order by payment.staff_id asc;
-- the exercise doesnt instruct to display the staff_id itself, but i display it