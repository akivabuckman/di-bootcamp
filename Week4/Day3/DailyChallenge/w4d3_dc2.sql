CREATE TABLE items(
	price INTEGER NOT NULL,
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(50) NOT NULL
);

CREATE TABLE product_orders(
	order_id SERIAL PRIMARY KEY,
)