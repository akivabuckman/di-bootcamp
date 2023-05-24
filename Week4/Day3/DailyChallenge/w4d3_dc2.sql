CREATE TABLE product_orders(
	order_id SERIAL PRIMARY KEY,
	order_date DATE NOT NULL
);

CREATE TABLE items(
	price INTEGER NOT NULL,
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR(50) NOT NULL,
	fk_order_id INTEGER NOT NULL,
	FOREIGN KEY (fk_order_id) REFERENCES product_orders(order_id) ON DELETE CASCADE
);


CREATE OR REPLACE FUNCTION total_price(oid INTEGER)
RETURNS INTEGER AS $total$
BEGIN
	RETURN(SELECT SUM(price) FROM items WHERE items.fk_order_id = oid);
END;
$total$ LANGUAGE plpgsql;