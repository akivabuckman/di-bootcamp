from menu_manager import MenuManager
import psycopg2 as ps


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"INSERT INTO menu_items (item_name, item_price) VALUES('{self.name}', '{self.price}');"
        cursor.execute(query)
        connection.commit()

    def delete(self):
        query = f"DELETE FROM menu_items WHERE item_name = '{self.name}' AND item_price = {self.price};"
        cursor.execute(query)
        connection.commit()

    def update(self, name, price):
        new_name = name
        new_price = price
        query = f"UPDATE menu_items " \
                f"SET item_name = '{new_name}', item_price = {new_price} " \
                f"WHERE item_name = '{self.name}' and item_price = {self.price}"
        self.name = new_name
        self.price = new_price
        cursor.execute(query)
        connection.commit()


def connect_sql():
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = '1234'
    DATABASE = 'menu'
    connection = ps.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname = DATABASE)
    cursor = connection.cursor()
    return (cursor, connection)

def add_item_to_menu(name, price):
    # try:
    item = MenuItem(name, price)

    # else:
    print("item was added successfully")
    return item

(cursor, connection) = connect_sql()
# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item = MenuItem('Beef Stew', 11)
# item.save()
item2 = MenuManager()
item2.get_by_name('Beef Stew')
