import faker
from login import Login
from menu import Menu
import recipe_manager

def main():
    active_user = Login().login # initiates login, returns username
    menu_choice = Menu().display_menu(active_user) # displays menu, returns function to run (user choice)
    if menu_choice == 'logout':
        main()
    else:
        menu_choice() # runs the function the user chose in previous line
# class User:
#     user_list = []
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#
#
#     @classmethod
#     def create_fake_users(cls,amount):
#         for i in range(amount):
#             username =
#             user = User()
main()