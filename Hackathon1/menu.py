import recipe_manager
# import main
class Menu:
    def display_menu(self, active_user):
        print(f"\nHey {active_user}, what would you like to do?")
        print("(A)dd New Recipe")
        print("(S)earch All Recipes")
        print("(U)pdate Existing Recipe")
        print("(V)iew Favorite Recipes")
        function_dict = {
            'a': recipe_manager.Recipe.add_new_recipe,
            's': recipe_manager.search_all_recipes,
            'u': recipe_manager.Recipe.update_existing_recipe,
            'v': recipe_manager.view_favorite_recipes,
            'l': 'logout'
        }
        while True:
            menu_choice = input("(L)ogout: ").lower()
            if menu_choice in "asuvl":
                return function_dict[menu_choice]
            else:
                print("Chose A, S, U, V, or L!")
                continue
