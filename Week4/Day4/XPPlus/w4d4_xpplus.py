import psycopg2

def parts_1_2():
    users = {
        "anna": "a"*5,
        "bob": "b"*5,
        "carl": "c"*5
    }


    while True:
        user_choice = input("exit or login? ").lower()
        if user_choice == "exit":
            break
        elif user_choice == "login":
            given_username = input("username: ")
            given_pw = input("password: ")
            if given_username in users:
                if users[given_username] == given_pw:
                    print("you are now logged in")
                    logged_in = given_username
                else:
                    print("wrong password")
            else:
                sign_up_choice = input("username doesnt exist. sign up? y/n: ")
                if sign_up_choice == 'n':
                    break
                elif sign_up_choice == 'y':
                    new_username = input("enter new username: ")
                    new_password = input("enter new password: ")
                    users[new_username] = new_password

# PART 3
connection = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='w4d4_xpplus')
cursor = connection.cursor()
create_db = """CREATE DATABASE w4d4_xpplus
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;"""

# cursor.execute(create_db)
# connection.commit()
# cursor.close()

# create_table = """CREATE TABLE users (
#     username VARCHAR(50) NOT NULL,
#     password VARCHAR(50) NOT NULL);
# """
# cursor.execute(create_table)
# connection.commit()
# cursor.close()

# insert_query = """
# INSERT INTO users(username, password) VALUES
# ('anna', 'aaaaa'), ('bob', 'bbbbb'), ('carl', 'ccccc');
# """
# cursor.execute(insert_query)
# connection.commit()
# cursor.close()

cursor.execute("SELECT username FROM users")
users = [i[0] for i in cursor.fetchall()]
while True:
    user_choice = input("exit or login? ").lower()
    if user_choice == "exit":
        break
    elif user_choice == "login":
        given_username = input("username: ")
        given_pw = input("password: ")
        if given_username in users:
            if users[given_username] == given_pw:
                print("you are now logged in")
                logged_in = given_username
            else:
                print("wrong password")
        else:
            sign_up_choice = input("username doesnt exist. sign up? y/n: ")
            if sign_up_choice == 'n':
                break
            elif sign_up_choice == 'y':
                new_username = input("enter new username: ")
                new_password = input("enter new password: ")
                cursor.execute(f"INSERT INTO users(username, password) VALUES ('{new_username}', '{new_password}');")
                connection.commit()
                cursor.close()