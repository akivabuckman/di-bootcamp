select rating, count(rating)
from film
group by rating;

select title
from film
where rating in ('G', 'PG-13');

select title
from film
where rating in ('G', 'PG-13') and
length < 120 and
rental_rate < 3
order by title asc;

update customer
set first_name = 'Akiva', last_name = 'Buckman'
where customer_id = 3;

update address
set address ='1213 Made Up St.'
where address_id = (select address_id from customer where customer_id = 3);