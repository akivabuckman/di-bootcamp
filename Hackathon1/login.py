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
        self.usernames = [i[1] for i in user_db]
        self.fake = faker.Faker()

    def login(self):
        given_user = input("Username: ")
        if given_user not in self.usernames:
            signup = input("That username doesn't exist. Sign up? Y/N: ").lower()
            if signup == 'y':
                faker_choice = input("Should I generate random info for you? Y/N: ").lower()
                if faker_choice != 'y':
                    new_username = input("Enter new username: ")
                    new_password = input("Enter new password: ")
                    new_diet_code = input("Enter diet code. 0: None, 1: Vegetarian, 2: Vegan, 3: Celiac ")
                    self.cursor.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{new_username}', "
                                        f"'{new_password}', '{new_diet_code}');")
                    self.connection.commit()
                    return new_username
                else:
                    new_username = self.fake.first_name()
                    new_password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation)
                                           for _ in range(10))
                    random_diet = random.randrange(0, 4)
                    print(f"Your username is {new_username}, your password is {new_password}, your diet code is "
                          f"{random_diet}.")
                    self.cursor.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{new_username}', "
                                        f"'{new_password}', '{random_diet}');")
                    self.connection.commit()
                    return new_username
            else:
                self.login()
        else:
            while True:
                given_password = input("Password: ")
                self.cursor.execute(f"SELECT password FROM users WHERE username = '{given_user}'")
                correct_password = self.cursor.fetchall()[0][0]
                if correct_password == given_password:
                    print(f"Welcome {given_user}, you're now logged in.")
                    return given_user
                else:
                    print("Wrong password")
