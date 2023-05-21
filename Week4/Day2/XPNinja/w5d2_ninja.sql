select store_id, first_name, last_name, email, address_id, activebool, create_date, last_update, active
from customer
order by last_name desc -- unspecified in exercise if to order by first or last
limit 2;

delete from payment
where customer_id = (select customer_id from customer where first_name = 'Scott');

-- yes, the deletion was from the payment table, not the customer table

select * from customer where first_name = 'Scott';

select *
from customer
left outer join payment
on customer.customer_id = payment.customer_id;
-- in the exercise it says scott's name should be null, but the payment details are null because his payments were deleted. unclear.

select *
from customer
right outer join payment
on customer.customer_id = payment.customer_id;