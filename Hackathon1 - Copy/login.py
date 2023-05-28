import psycopg2
import faker
import random
import string
import tkinter as tk

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='hackathon1')
CURSOR = CONNECTION.cursor()
class Login:
    def __init__(self):
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = '1234'
        DATABASE = 'hackathon1'
        # CONNECTION = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        CURSOR = CONNECTION.cursor()
        CURSOR.execute("SELECT * FROM users")
        user_db = CURSOR.fetchall()
        self.usernames = [i[1].lower() for i in user_db]
        self.fake = faker.Faker()

    @property
    def login(self):
        login_window = tk.Tk()
        login_window.title('Hello Python')
        login_window.geometry("300x200+10+20")
        login_window.mainloop()
        given_user = input("Hey there!\nEnter Username: ")
        if given_user.lower() not in self.usernames:
            signup = input("That username doesn't exist. Sign up? Y or any key: ").lower()
            if signup == 'y':
                faker_choice = input("Should I generate random info for you? Y or any key: ").lower()
                if faker_choice != 'y':
                    valid_user = False
                    while not valid_user:
                        new_username = input("Enter new username: ")
                        if new_username == '':
                            print("That's blank!\n")
                        else:
                            valid_user = True
                    valid_pw = False
                    while not valid_pw:
                        new_password = input("Enter new password: ")
                        if new_password == '':
                            print("That's blank!\n")
                            continue
                        else:
                            valid_pw = True
                    while True:
                        new_diet_code = input("Enter diet code. 0: None, 1: Vegetarian, 2: Vegan, 3: Celiac ")
                        if new_diet_code not in ['0', '1', '2', '3']:
                            print("Choose 0, 1, 2, or 3!")
                            continue
                        else:
                            break
                    CURSOR.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{new_username}', "
                                        f"'{new_password}', '{new_diet_code}');")
                    CONNECTION.commit()
                    return new_username
                else:
                    new_username = self.fake.first_name() + str(random.randint(1,1000))
                    CURSOR.execute("SELECT username FROM users")
                    existing_names = [i[0] for i in CURSOR.fetchall()]
                    if new_username in existing_names:
                        new_username += str(random.randint(1,1000))
                    new_password = ''.join(random.choice(string.ascii_letters + string.digits)
                                           for _ in range(10))
                    random_diet = int(random.choice("000000011223"))
                    print(f"Your username is {new_username}, your password is {new_password}, your diet code is "
                          f"{random_diet}.")
                    CURSOR.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{new_username}', "
                                        f"'{new_password}', '{random_diet}');")
                    CONNECTION.commit()
                    return new_username
            else:
                self.login()
        else:
            while True:
                given_password = input("Password: ")
                CURSOR.execute(f"SELECT password FROM users WHERE username ILIKE '{given_user}'")
                correct_password = CURSOR.fetchall()[0][0]
                if correct_password == given_password:
                    print(f"Welcome {given_user}, you're now logged in.")
                    return given_user
                else:
                    print("Wrong password")
