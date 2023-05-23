class Menu:
    def display_menu(self, active_user):
        print(f"Hey {active_user}, what would you like to do?")
        print("(A)dd Recipe")
        menu_choice = input("(S)earch Recipes: ")
