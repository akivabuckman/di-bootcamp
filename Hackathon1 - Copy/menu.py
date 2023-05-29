import recipe_manager
import tkinter as tk


class Menu:
    def display_menu(self, active_user):
        self.menu_screen = tk.Tk()
        self.menu_screen.title(f"Welcome {active_user}")
        label1 = tk.Label(text=f"Hey {active_user}, what would you like to do?")
        add_button = tk.Button(text="Add New Recipe", command=lambda: self.return_func('a'))
        search_button = tk.Button(text="Search Recipe Database", command=lambda: self.return_func('s'))
        view_button = tk.Button(text="View Favorite Recipes", command=lambda: self.return_func('v'))
        logout_button = tk.Button(text="Log Out", command=lambda: self.return_func('l'))
        label1.grid(row=0, column=0, columnspan=4, pady=5, padx=5)
        add_button.grid(row=1, column=0, padx=5, pady=5)
        search_button.grid(row=1, column=1, padx=5, pady=5)
        view_button.grid(row=1, column=2, padx=5, pady=5)
        logout_button.grid(row=1, column=3, padx=5, pady=5)
        self.menu_screen.mainloop()
        return self.chosen_func
    def return_func(self, menu_choice):
        self.menu_screen.destroy()
        function_dict = {
            'a': recipe_manager.RecipeManager.create_user_recipe,
            's': recipe_manager.RecipeManager.get_search_parameters,
            'v': recipe_manager.RecipeManager.view_favorites,
            'l': 'logout'
        }
        self.chosen_func = function_dict[menu_choice]
