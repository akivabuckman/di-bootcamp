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
        self.login_window = tk.Tk()
        self.login_window.title('Recipe Manager')
        self.login_window.geometry("300x200")
        self.hey = tk.Label(self.login_window, text="Hey There!")
        self.hey.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.user_label = tk.Label(self.login_window, text="Username:")
        self.pw_label = tk.Label(self.login_window, text="Password:")
        self.user_entry = tk.Entry(self.login_window)
        self.user_entry.focus()
        self.pw_entry = tk.Entry(self.login_window)
        self.user_label.grid(row=1, column=0, padx=10, pady=10)
        self.pw_label.grid(row=2, column=0, padx=10, pady=10)
        self.user_entry.grid(row=1, column=1, padx=10, pady=10)
        self.pw_entry.grid(row=2, column=1, padx=10, pady=10)
        self.login_button = tk.Button(text="Sign In", command=self.validate)
        self.login_button.grid(row=3, column=0)
        self.register_button = tk.Button(text="Register", command=self.register)
        self.register_button.grid(row=3, column=1)
        self.login_window.mainloop()
        return self.chosen_username

    def register(self):
        self.login_window.destroy()
        self.register_window = tk.Tk()
        self.register_window.title("New User")
        # self.register_window.geometry("300x100")
        self.q = tk.Label(text="Enter your own info, or generate random info?", pady=10, padx=10)
        self.own = tk.Button(text="My Info", command=self.user_info)
        self.random = tk.Button(text="Random Info", command=self.random_info)
        self.q.grid(row=0, column=0, columnspan=2)
        self.own.grid(row=1, column=0)
        self.random.grid(row=1, column=1)

    def random_info(self):
        self.register_window.destroy()
        self.user_info_screen = tk.Tk()
        self.user_info_screen.title("Random Info Generator")
        self.chosen_username = self.fake.first_name() + str(random.randint(1, 1000))
        CURSOR.execute("SELECT username FROM users")
        existing_names = [i[0] for i in CURSOR.fetchall()]
        if self.chosen_username in existing_names:
            self.chosen_username += str(random.randint(1001, 2000))
        new_password = ''.join(random.choice(string.ascii_letters + string.digits)
                               for _ in range(10))
        random_diet = int(random.choice("000000011223"))
        info_label = tk.Label(text=f"Your username is {self.chosen_username}\nYour password is {new_password}\n"
                                   f"Your diet code is {random_diet}.")
        info_label.grid(row=0, column=0, padx=5, pady=5)
        cont_button = tk.Button(text="OK", command=self.user_info_screen.destroy)
        cont_button.grid(row=1, column=0, padx=5, pady=5)
        CURSOR.execute(f"INSERT INTO users(username, password, diet_code) VALUES ('{self.chosen_username}', "
                       f"'{new_password}', '{random_diet}');")
        CONNECTION.commit()

    def user_info(self):
        self.register_window.destroy()
        self.user_info_screen = tk.Tk()
        self.user_info_screen.title = "Register New User"
        self.new_username_label = tk.Label(text="New Username:")
        self.new_pw_label = tk.Label(text="New Password:")
        self.new_username_entry = tk.Entry(self.user_info_screen)
        self.new_pw_entry = tk.Entry(self.user_info_screen)
        new_diet_code_label = tk.Label(text="Enter diet code. 0: None, \n1: Vegetarian, 2: Vegan, 3: Celiac")
        self.new_username_label.grid(row=0, column=0, padx=5, pady=5)
        self.new_pw_label.grid(row=1, column=0, padx=5, pady=5)
        self.new_username_entry.grid(row=0, column=1, padx=5, pady=5)
        self.new_pw_entry.grid(row=1, column=1, padx=5, pady=5)
        new_diet_code_label.grid(row=2, column=0, padx=5, pady=5)
        self.new_diet_entry = tk.Entry(self.user_info_screen)
        self.new_diet_entry.grid(row=2, column=1, padx=5, pady=5)
        self.register_button = tk.Button(text='Register and Log In', command=self.register_and_log_in)
        self.register_button.grid(row=3, columnspan=2)
        self.username_error = tk.Label(text='', fg='red')
        self.username_error.grid(row=4, columnspan=2)

    def register_and_log_in(self):
        self.chosen_username = self.new_username_entry.get()
        chosen_pw = self.new_pw_entry.get()
        chosen_diet = self.new_diet_entry.get()
        CURSOR.execute("SELECT username from users;")
        taken_usernames = [i[0].lower() for i in CURSOR.fetchall()]
        if self.new_username_entry.get().lower() in taken_usernames:
            self.username_error.config(text="That username is taken. Choose another.")
        elif self.new_username_entry.get() == '':
            self.username_error.config(text="Username can't be blank!")
        elif self.new_pw_entry.get() == '':
            self.username_error.config(text="Password can't be blank!")
        elif self.new_diet_entry.get() not in ['0', '1', '2', '3']:
            self.username_error.config(text="For Diet Code pick 0, 1, 2, or 3")
        else:
            self.user_info_screen.destroy()
            CURSOR.execute(f"INSERT INTO users(username, password, diet_code) "
                           f"VALUES ('{self.chosen_username}', "
                           f"'{chosen_pw}', '{chosen_diet}');")
            CONNECTION.commit()


    def validate(self):
        given_user = self.user_entry.get()
        if given_user.lower() not in self.usernames:
            self.login_error = tk.Label(self.login_window, text="That username doesn't exist. Please Register",
                                        fg="red")
            self.login_error.grid(row=4, column=0, columnspan=2)
        else:
            given_password = self.pw_entry.get()
            CURSOR.execute(f"SELECT password FROM users WHERE username ILIKE '{given_user}'")
            correct_password = CURSOR.fetchall()[0][0]
            if correct_password == given_password:
                return given_user
            else:
                self.login_error.config(text="Password incorrect.")

        self.login_window.mainloop()
