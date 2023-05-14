# 🌟 Exercise 1: Import
# Instructions
# In a file named func.py create a function that adds 2 number, and prints the result
# In a file namedexercise_one.py import and the function
def xpplus1():
    def add_numbers(num1, num2):
        return num1 + num2


# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.
import random


def xpplus2():
    def compare(chosen_num):
        rand_num = random.randint(1, 100)
        if chosen_num == rand_num:
            print("Success")


# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
def xpplus3():
    import random
    import string
    print(''.join(random.choice(string.ascii_letters) for i in range(5)))


# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
def xpplus4():
    from datetime import datetime
    print(datetime.now().date())


# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def xpplus5():
    from datetime import datetime
    jan1 = datetime.strptime("2024/01/01", "%Y/%m/%d")
    today = datetime.now()
    print(jan1 - today)


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message
# stating how many minutes the user lived in his life.
def xpplus6():
    from datetime import datetime
    birthday = datetime.strptime(input('Enter birthday YYYY/MM/DD: '), "%Y/%m/%d")
    print((datetime.now() - birthday).days)


# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming holiday and print which
# holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
def xpplus7():
    from datetime import datetime
    print(datetime.now())
    next_holiday = {"name": "Shavuot",
                    "date": datetime.strptime("2023/05/26", "%Y/%m/%d"),
                    "time_from_now": datetime.strptime("2023/05/26", "%Y/%m/%d") - datetime.now()}
    print(f"{next_holiday['name']} is in {next_holiday['time_from_now'].days} days and "
          f"{int(next_holiday['time_from_now'].seconds / 3600)} hours")


# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years
# old.
def xpplus8():
    def calculate(seconds):
        earth = seconds / 31557600
        results = {
            'earth': earth,
            'mercury': 0.2408467 * earth,
            'venus': 0.61519726 * earth,
            'mars': 1.8808158 * earth,
            'jupiter': 11.862615 * earth,
            'saturn': 29.447498 * earth,
            'uranus': 84.016846 * earth,
            'neptune': 164.79132 * earth,
        }
        return results


# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress,
# langage_code. Use faker to populate them with fake data.

def xpplus9():
    from faker import Faker

    fake = Faker()
    users = []

    def add_user():
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        return user

xpplus2()