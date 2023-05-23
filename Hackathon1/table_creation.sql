-- Database: hackathon1

-- DROP DATABASE IF EXISTS hackathon1;

-- CREATE DATABASE hackathon1
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- CREATE TABLE diets (
-- 	diet_code INTEGER NOT NULL PRIMARY KEY,
-- 	diet_name VARCHAR(20) NOT NULL
-- );

-- CREATE TABLE recipes (
-- 	recipe_name VARCHAR(50) NOT NULL,
-- 	recipe_id SERIAL PRIMARY KEY,
-- 	ingredients TEXT,
-- 	instructions TEXT,
-- 	cook_time INTEGER,
-- 	cuisine VARCHAR(50),
-- 	diet_code INTEGER,
-- 	FOREIGN KEY (diet_code) REFERENCES diets(diet_code)
-- );

-- CREATE TABLE users (
-- 	user_id SERIAL PRIMARY KEY,
-- 	username VARCHAR(50) NOT NULL,
-- 	password VARCHAR(50) NOT NULL,
-- 	diet_code INTEGER,
-- 	FOREIGN KEY (diet_code) REFERENCES diets(diet_code)
-- );

-- CREATE TABLE user_recipe (
-- 	recipe_id INTEGER NOT NULL,
-- 	user_id INTEGER NOT NULL,
-- 	PRIMARY KEY (recipe_id, user_id),
-- 	FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
-- 	FOREIGN KEY (user_id) REFERENCES users(user_id)
-- );

-- INSERT INTO diets(diet_code, diet_name) VALUES
-- (0, 'None'), (1, 'Vegetarian'), (2, 'Vegan'), (3, 'Celiac');