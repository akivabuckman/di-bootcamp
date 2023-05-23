import psycopg2
import faker
import random
import string


class Login:
    def __init__(self):
        HOSTNAME = 'localhost'
        USERNAME = 'postgres'
        PASSWORD = '1234'
        DATABASE = 'hackathon1'
        self.connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM users")
        user_db = self.cursor.fetchall()
        self.usernames = [i[1].lower() for i in user_db]
        self.fake = faker.Faker()

    @property
    def login(self):
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
                    valid_dc = False
                    while not valid_dc:
                        new_diet_code = input("Enter diet code. 0: None, 1: Vegetarian, 2: Vegan, 3: Celiac ")
                        if new_diet_code not in ['0', '1', '2', '3']:
                            print("Choose 0, 1, 2, or 3!")
                            continue
                        else:
                            valid_dc = True
                    self.cursor.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{new_username}', "
                                        f"'{new_password}', '{new_diet_code}');")
                    self.connection.commit()
                    return new_username
                else:
                    new_username = self.fake.first_name()
                    new_password = ''.join(random.choice(string.ascii_letters + string.digits)
                                           for _ in range(10))
                    random_diet = int(random.choice("000000011223"))
                    print(f"Your username is {new_username}, your password is {new_password}, your diet code is "
                          f"{random_diet}.")
                    self.cursor.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{new_username}', "
                                        f"'{new_password}', '{random_diet}');")
                    self.connection.commit()
                    return new_username
            else:
                self.login
        else:
            while True:
                given_password = input("Password: ")
                self.cursor.execute(f"SELECT password FROM users WHERE username ILIKE '{given_user}'")
                # a = (self.cursor.fetchall())
                # b = self.cursor.fetchall()
                # print(a)
                # print(b)
                # print(a[0])
                # print(a[0][0])
                correct_password = self.cursor.fetchall()[0][0]
                if correct_password == given_password:
                    print(f"Welcome {given_user}, you're now logged in.")
                    return given_user
                else:
                    print("Wrong password")
