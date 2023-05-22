-- EXERCISE 1
-- 1
SELECT name
FROM language;

-- 2A
SELECT title, description, language.name
FROM film
LEFT OUTER JOIN language
ON film.language_id = language.language_id;

-- 2B
SELECT title, description, language.name
FROM film
RIGHT OUTER JOIN language
ON film.language_id = language.language_id;

-- 3
-- CREATE TABLE new_film (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR (50) NOT NULL
-- );

-- INSERT INTO new_film (name)
-- VALUES ('Shrek');

-- INSERT INTO new_film (name)
-- VALUES ('Toy Story');

-- 4
-- CREATE TABLE customer_review (
-- 	review_id SERIAL,
-- 	fk_film_id INTEGER NOT NULL,
-- 	language_id INTEGER,
-- 	title VARCHAR (50),
-- 	score SMALLINT,
-- 	review_text TEXT,
-- 	last_update DATE,
-- 	PRIMARY KEY (review_id),
-- 	FOREIGN KEY (fk_film_id) REFERENCES new_film(id) ON DELETE CASCADE
-- );

-- 5
-- INSERT INTO customer_review (fk_film_id, language_id, title, score, review_text, last_update)
-- VALUES (1, 1, 'Shrek Review', 2, 'shrek is too green', '1991-01-01');

-- INSERT INTO customer_review (fk_film_id, language_id, title, score, review_text, last_update)
-- VALUES (2, 1, 'Toy Story Review', 9, 'yay woody', '2001-01-01');

-- 6
-- DELETE FROM new_film WHERE name = 'Shrek';
-- SELECT * FROM customer_review; -- the Shrek review is deleted because the fk of customer_review was set to ON DELETE CASCADE

-- EXERCISE 2
-- 1
-- UPDATE film
-- SET language_id = 2
-- WHERE film_id BETWEEN 11 AND 15;

-- 2
-- In the customer table, address_id is a FK, connected to the address table. On update it cascades and on delete it restricts.
-- When we INSERT into the customer table, the address_id must be unique.

-- 3
DROP TABLE IF EXISTS customer_review;
-- This was easy, because customer_review relies on film_id, and not vice versa.

-- 4
SELECT COUNT(*) FROM rental
WHERE return_date IS NULL;

-- 5
SELECT title, rental_rate
FROM film
INNER JOIN (SELECT * FROM rental LEFT OUTER JOIN inventory ON rental.inventory_id = inventory.inventory_id WHERE rental.return_date IS NULL) as not_returned
ON film.film_id = not_returned.film_id
ORDER BY film.rental_rate DESC
LIMIT 30;

-- 6A
SELECT *
FROM film
WHERE description ILIKE '%sumo%';

-- tools:
SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe'; --returns actor id of penelope
SELECT film_id FROM film_actor WHERE actor_id = (SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe'); -- returns movies with penelope
SELECT film_id FROM film WHERE description ILIKE '%sumo%'; -- returns film_id's with sumo in description

-- returns film_id of final answer:
SELECT penelope_movies.film_id
FROM (SELECT film_id FROM film_actor WHERE actor_id = (SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe')) AS penelope_movies
INNER JOIN (SELECT film_id FROM film WHERE description ILIKE '%sumo%') AS sumo_movies
ON penelope_movies.film_id = sumo_movies.film_id;

-- Final query:
SELECT title
FROM film
WHERE film_id = (SELECT penelope_movies.film_id
FROM (SELECT film_id FROM film_actor WHERE actor_id = (SELECT actor_id FROM actor WHERE first_name = 'Penelope' AND last_name = 'Monroe')) AS penelope_movies
INNER JOIN (SELECT film_id FROM film WHERE description ILIKE '%sumo%') AS sumo_movies
ON penelope_movies.film_id = sumo_movies.film_id);

-- 6B
SELECT category_id FROM category WHERE name = 'Documentary'; -- returns category id for documentary
SELECT film_id FROM film_category where category_id = (SELECT category_id FROM category WHERE name = 'Documentary'); -- returns all documentary film id's

-- Final query:
SELECT title
FROM film
WHERE film_id in (SELECT film_id FROM film_category where category_id = (SELECT category_id FROM category WHERE name = 'Documentary'))
AND length < 60
AND rating = 'R';

-- 6C
-- Steps
-- SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan'; -- returns matthew's customer id

-- SELECT inventory_id FROM rental WHERE customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan')
-- AND return_date BETWEEN '2005/07/28' AND '2005/08/01'; -- returns matthews rentals between given dates

-- SELECT film_id FROM inventory WHERE inventory_id IN (SELECT inventory_id FROM rental WHERE customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan')
-- AND return_date BETWEEN '2005/07/28' AND '2005/08/01'); -- returns film id's of matthew's rentals between given dates

-- Final Query
SELECT title FROM film WHERE film_id IN (SELECT film_id FROM inventory WHERE inventory_id IN (SELECT inventory_id FROM rental WHERE customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan')
AND return_date BETWEEN '2005/07/28' AND '2005/08/01'))
AND rental_rate > 4;

-- 6D
-- SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan'; -- returns matthew's customer id

-- SELECT inventory_id FROM rental WHERE customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan'); 
-- -- returns matthews inventory id's

-- SELECT film_id FROM inventory WHERE inventory_id IN (SELECT inventory_id FROM rental WHERE customer_id = (SELECT customer_id FROM customer WHERE first_name = 'Matthew' AND last_name = 'Mahan'));
-- -- returns matthew's film id's

-- Final query
SELECT title
FROM film
WHERE film_id IN (SELECT film_id FROM inventory WHERE inventory_id IN (SELECT inventory_id FROM rental WHERE customer_id = 
																	   (SELECT customer_id FROM customer WHERE first_name = 'Matthew' 
																		AND last_name = 'Mahan')))
AND title ILIKE '%boat%' OR description ILIKE '%boat%'
AND replacement_cost > 25
ORDER BY replacement_cost DESC;