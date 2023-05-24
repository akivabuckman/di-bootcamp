import faker
from login import Login
from menu import Menu
import recipe_manager

def main():
    while True:
        active_user = Login().login # initiates login, returns username
        while True:
            menu_choice = Menu().display_menu(active_user) # displays menu, returns function to run (user choice)
            if menu_choice == 'logout':
                break
            else:
                menu_choice(active_user) # runs the function the user chose in previous line
main()