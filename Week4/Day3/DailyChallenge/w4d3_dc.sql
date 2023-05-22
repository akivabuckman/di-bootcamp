-- PART I
-- 1
-- CREATE TABLE customer (
-- 	id SERIAL,
-- 	first_name VARCHAR(50) NOT NULL,
-- 	last_name VARCHAR(50) NOT NULL,
-- 	PRIMARY KEY (id)
-- );

-- CREATE TABLE customer_profile (
-- 	pk_id INTEGER NOT NULL,
-- 	isLoggedIn BOOLEAN DEFAULT FALSE,
-- 	PRIMARY KEY (pk_id),
-- 	CONSTRAINT fk_customer_id FOREIGN KEY (pk_id) REFERENCES customer (id)
-- );

-- 2
-- INSERT INTO customer (first_name, last_name)
-- VALUES ('John', 'Doe'), ('Jerome', 'Lalu'), ('Lea', 'Rive');

-- 3
-- INSERT INTO customer_profile (pk_id, isLoggedIn) VALUES
-- ((SELECT id from customer where first_name = 'John' and last_name = 'Doe'), True)

-- INSERT INTO customer_profile (pk_id, isLoggedIn) VALUES
-- ((SELECT id from customer where first_name = 'Jerome' and last_name = 'Lalu'), False)

-- 4A
SELECT first_name
FROM customer
INNER JOIN customer_profile
ON customer_profile.pk_id = customer.id
AND customer_profile.isLoggedIn = True;

-- 4B
SELECT customer.first_name, customer_profile.isLoggedIn
FROM customer
LEFT OUTER JOIN customer_profile
ON customer.id = customer_profile.pk_id;

-- 4C
SELECT COUNT(*)
FROM customer_profile
WHERE isLoggedIn = FALSE;

-- PART II
-- 1
-- CREATE TABLE book (
-- 	book_id SERIAL PRIMARY KEY,
-- 	title VARCHAR (50) NOT NULL,
-- 	author VARCHAR (50) NOT NULL
-- );

-- 2
-- INSERT INTO book (title, author) VALUES
-- ('Alice in Wonderland', 'Lewis Carroll'), ('Harry Potter', 'J.K Rowling'), ('To Kill a Mockingbird', 'Harper Lee');

-- 3
-- CREATE TABLE student (
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL UNIQUE,
-- 	age SMALLINT CHECK (age <= 15)
-- )

-- 4
-- INSERT INTO student (name, age) VALUES
-- ('John', 12), ('Lera', 11), ('Patrick', 10), ('Bob', 14);

-- 5
-- CREATE TABLE library (
-- 	borrowed_date DATE NOT NULL,
-- 	book_fk_id INTEGER NOT NULL, -- connect to book_id
-- 	student_fk_id INTEGER NOT NULL, -- connect to student_id
-- 	PRIMARY KEY (book_fk_id, student_fk_id),
-- 	FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON UPDATE CASCADE ON DELETE CASCADE,
-- 	FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON UPDATE CASCADE ON DELETE CASCADE
-- )

-- 6
-- INSERT INTO library (borrowed_date, book_fk_id, student_fk_id) VALUES
-- ('02/15/2022', 
-- (SELECT book_id FROM book WHERE title = 'Alice in Wonderland'),
-- (SELECT student_id FROM student WHERE name = 'John')),
-- ('03/03/2021',
-- (SELECT book_id FROM book WHERE title = 'To Kill a Mockingbird'),
-- (SELECT student_id FROM student WHERE name = 'Bob')),
-- ('05/23/2021',
-- (SELECT book_id FROM book WHERE title = 'Alice in Wonderland'),
-- (SELECT student_id FROM student WHERE name = 'Lera')),
-- ('08/12/2021',
-- (SELECT book_id FROM book WHERE title = 'Harry Potter'),
-- (SELECT student_id FROM student WHERE name = 'Bob'));
 
-- 7
SELECT student_fk_id FROM library;

SELECT student.name, book.title
FROM student
INNER JOIN library
ON library.student_fk_id = student.student_id
INNER JOIN book
ON library.book_fk_id = book.book_id;

SELECT AVG(student.age)
FROM student
INNER JOIN library
ON library.student_fk_id = student.student_id
INNER JOIN book
ON library.book_fk_id = book.book_id
AND book.title = 'Alice in Wonderland';

DELETE FROM student WHERE name='John';
SELECT * FROM library;
-- All rows with John's borrows were deleted, as per the CASCADE.