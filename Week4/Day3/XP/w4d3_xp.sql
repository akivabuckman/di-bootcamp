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

SELECT * FROM public.rental
WHERE return_date IS NULL;