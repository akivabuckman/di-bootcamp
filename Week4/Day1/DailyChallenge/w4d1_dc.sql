select count(*) from actors;

insert into actors (first_name, last_name, birthday, number_oscars) values (null, null, null, null); -- returns error because
-- some of the columns were defined as not-nulls