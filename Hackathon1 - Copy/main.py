import faker
from login import Login
from menu import Menu
import tkinter as tk


def main():
    while True:
        active_user = Login().login # initiates login, returns username
        while True:
            menu_choice = Menu().display_menu(active_user) # displays menu, returns function to run (user choice)
            if menu_choice == 'logout':
                break
            else:
                menu_choice(active_user) # runs the function the user chose in previous line
# main()

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

for i in people:
    print(i)