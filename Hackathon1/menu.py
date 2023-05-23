class Menu:
    def display_menu(self, active_user):
        print(f"Hey {active_user}, what would you like to do?")
        print("(A)dd New Recipe")
        print("(S)earch All Recipes")
        print("(U)pdate Existing Recipe")
        print("(V)iew Saved Recipes")
        menu_choice = input("(L)ogout: ").lower()
        return menu_choice
