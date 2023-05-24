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
        cursor.execute(f"SELECT * FROM menu_items WHERE item_name = '{self.name}' AND item_price = {self.price};")
        if len(cursor.fetchall()) == 0:
            print("No items found")
        else:
            query = f"DELETE FROM menu_items WHERE item_name = '{self.name}' AND item_price = {self.price};"
            cursor.execute(query)
            connection.commit()
            print("Item removed successfully")

    def update(self, new_name, new_price, old_name, old_price):
        cursor.execute(f"SELECT * FROM menu_items WHERE item_name = '{old_name}' AND item_price = {old_price};")
        if len(cursor.fetchall()) == 0:
            print("No items found")
        else:
            query = f"UPDATE menu_items " \
                    f"SET item_name = '{new_name}', item_price = {new_price} " \
                    f"WHERE item_name = '{old_name}' and item_price = {old_price}"
            self.name = new_name
            self.price = new_price
            cursor.execute(query)
            connection.commit()
            print("Item updated successfully")

def connect_sql():
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = '1234'
    DATABASE = 'menu'
    connection = ps.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    return (cursor, connection)


def add_item_to_menu(name, price):
    item = MenuItem(name, price)
    item.save()
    return item


def remove_item_from_menu(name, price):
    item = MenuItem(name, price)
    item.delete()
    return item

def update_item_from_menu():
    old_name = input("Name of old item to update? ")
    old_price = input("Price of old item to update? ")
    new_name = input("New name: ")
    new_price = input("New price: ")
    item = MenuItem(new_name, new_price)
    item.update(new_name, new_price, old_name, old_price)
    return item


def show_restaurant_menu():
    items = MenuManager.all_items()
    for i in items:
        print(f"{i[1]}: {i[2]}")


(cursor, connection) = connect_sql()
# item = MenuItem('Burger', 35)
# item.save()
# item.delete()
# item.update('Veggie Burger', 37)
# item = MenuItem('Beef Stew', 11)
# item.save()
# item2 = MenuManager()
# item2.get_by_name('Beef Stew')
# items = MenuManager.all_items()
