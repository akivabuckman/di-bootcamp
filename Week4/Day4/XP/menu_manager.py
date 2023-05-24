import psycopg2 as ps
# from menu_item import MenuItem

def connect_sql():
    HOSTNAME = 'localhost'
    USERNAME = 'postgres'
    PASSWORD = '1234'
    DATABASE = 'menu'
    connection = ps.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    return (cursor, connection)

(cursor, connection) = connect_sql()


class MenuManager:
    def get_by_name(self, name):
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}'"
        cursor.execute(query)
        results = cursor.fetchall()
        self.name = results[0][1]
        self.price = results[0][2]
        return self

    @classmethod
    def all_items(cls):
        query = "SELECT * FROM menu_items"
        cursor.execute(query)
        all = cursor.fetchall()
        return all
