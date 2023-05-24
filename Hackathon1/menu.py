import recipe_manager
# import main
class Menu:
    def display_menu(self, active_user):
        print(f"\nHey {active_user}, what would you like to do?")
        print("(A)dd New Recipe")
        print("(S)earch All Recipes")
        print("(V)iew Favorite Recipes")
        function_dict = {
            'a': recipe_manager.create_user_recipe,
            's': recipe_manager.get_search_parameters,
            'v': recipe_manager.view_favorites,
            'l': 'logout'
        }
        while True:
            menu_choice = input("(L)ogout: ").lower()
            if menu_choice in "asuvl":
                return function_dict[menu_choice]
            else:
                print("Chose A, S, U, V, or L!")
                continue
