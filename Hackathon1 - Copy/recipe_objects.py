import requests
import psycopg2
import smtplib
import tkinter as tk

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='hackathon1')
CURSOR = CONNECTION.cursor()
EDAMAM_ID = '7c239491'
EDAMAM_KEY = 'b2450a48ca06718b544940eb54b7acc2'

class Recipe:
    def return_now(self, current_screen):
        current_screen.destroy()

class APIRecipe(Recipe):
    def __init__(self, json_data):
        self.name = json_data['recipe']['label'].replace("'", '')
        self.ingredients = json_data['recipe']['ingredientLines']
        self.ingredients_string = ', '.join(self.ingredients).replace("'", '')
        self.cook_time = int(json_data['recipe']['totalTime'])
        self.cuisine = json_data['recipe']['cuisineType'][0].replace("'", '')
        self.diet_code = 3 if 'Celiac' in json_data['recipe']['healthLabels'] else \
            2 if 'Vegan' in json_data['recipe']['healthLabels'] else \
                1 if 'Vegetarian' in json_data['recipe']['healthLabels'] else 0

    def add_recipe_to_favorites(self, active_user, specific_api_screen, add_button):
        CURSOR.execute(f"INSERT INTO favorites(recipe_name, ingredients, cook_time, cuisine, diet_code) VALUES"
                       f"('{self.name}', '{self.ingredients_string}', '{self.cook_time}', '{self.cuisine}', "
                       f"'{self.diet_code}');")
        CONNECTION.commit()
        CURSOR.execute(f"INSERT INTO user_favorites(user_id, recipe_id) VALUES"
                       f"((SELECT user_id FROM users WHERE username ILIKE '{active_user}'),"
                       f"(SELECT recipe_id FROM favorites WHERE recipe_id = "
                       f"(SELECT MAX(recipe_id) FROM favorites)))")
        CONNECTION.commit()
        fav_added_label = tk.Label(specific_api_screen, text="Added to Favorites", fg='blue')
        fav_added_label.grid(row=7, column=0)
        try:
            add_button.destroy()
        except:
            pass


class UserRecipe(Recipe):
    def __init__(self, active_user):
        self.user_recipe_screen = tk.Tk()
        self.user_recipe_screen.title("Custom Recipe")
        label0 = tk.Label(text="Enter New Recipe Details")
        label0.grid(row=0, column=0, columnspan=2)
        label1 = tk.Label(text="Recipe Name:")
        label1.grid(row=1, column=0)
        self.name_entry = tk.Entry()
        self.name_entry.grid(row=1, column=1, pady=5)
        self.name_entry.focus()
        label2 = tk.Label(text="Cook Time [min]:")
        label2.grid(row=2, column=0)
        self.cook_time_entry = tk.Entry()
        self.cook_time_entry.grid(row=2, column=1)
        label3 = tk.Label(text="Cuisine:")
        label3.grid(row=3, column=0)
        self.cuisine_entry = tk.Entry()
        self.cuisine_entry.grid(row=3, column=1)
        label35 = tk.Label(text="Diet Code. 0: None, 1: Vegetarian")
        label35.grid(row=4, column=0, columnspan=2)
        label36 = tk.Label(text="2: Vegan, 3: Celiac:")
        label35.grid(row=5, column=0, columnspan=2)
        self.diet_entry = tk.Entry()
        self.diet_entry.grid(row=6, column=0, columnspan=2)
        label4 = tk.Label(text="Enter ingredients separated by commas:")
        label4.grid(row=7, column=0, columnspan=2)
        self.ingredients_entry = tk.Entry()
        self.ingredients_entry.grid(row=8, column=0, columnspan=2, pady=5)
        self.add_fav_button = tk.Button(text="Add to Favorites", command=lambda: self.validate_user_recipe(active_user))
        self.add_fav_button.grid(row=9, column=0, padx=5, columnspan=2, pady=5)
        self.error_message = tk.Label(text="", fg='red')
        self.error_message.grid(row=10, column=0, columnspan=2)
        self.user_recipe_screen.mainloop()

    def validate_user_recipe(self, active_user):
        if self.name_entry.get() == '':
            self.error_message.config(text="Recipe Name can't be blank")
        elif not self.cook_time_entry.get().isdigit():
            self.error_message.config(text="Cook time must be a number")
        elif self.diet_entry.get() not in ['0', '1', '2', '3']:
            self.error_message.config(text="Diet Code must be 0,1,2,3")
        else:
            self.name = self.name_entry.get()
            self.cook_time = self.cook_time_entry.get()
            self.cuisine = self.cuisine_entry.get()
            self.diet_code = self.diet_entry.get()
            self.ingredients = self.ingredients_entry.get().split(',')
            self.ingredients = [i.strip() for i in self.ingredients]
            self.ingredients_string = ', '.join(self.ingredients).replace("'", "")
            self.add_recipe_to_favorites(active_user, self.user_recipe_screen)
            self.user_recipe_screen.destroy()
    def add_recipe_to_favorites(self, active_user, specific_api_screen):
        CURSOR.execute(f"INSERT INTO favorites(recipe_name, ingredients, cook_time, cuisine, diet_code) VALUES"
                       f"('{self.name}', '{self.ingredients_string}', '{self.cook_time}', '{self.cuisine}', "
                       f"'{self.diet_code}');")
        CONNECTION.commit()
        CURSOR.execute(f"INSERT INTO user_favorites(user_id, recipe_id) VALUES"
                       f"((SELECT user_id FROM users WHERE username ILIKE '{active_user}'),"
                       f"(SELECT recipe_id FROM favorites WHERE recipe_id = "
                       f"(SELECT MAX(recipe_id) FROM favorites)))")
        CONNECTION.commit()
        # # input of new recipe details
        # self.name = input("\nRecipe Name: ").replace("'", '').title()
        # while True:
        #     self.cook_time = input("Cook time [min]: ")
        #     try:
        #         self.cook_time = int(self.cook_time)
        #     except ValueError:
        #         print("Enter an integer!")
        #         continue
        #     else:
        #         break
        # self.cuisine = input("Cuisine: ").replace("'", "")
        # while True:
        #     self.diet_code = input("Enter diet code. 0: None, 1: Vegetarian, 2: Vegan, 3: Celiac ")
        #     if self.diet_code not in ['0', '1', '2', '3']:
        #         print("Choose 0, 1, 2, or 3!")
        #         continue
        #     else:
        #         break
        # # ingredient entry:
        # self.ingredients = []
        # done = False
        # while not done:
        #     ingredient = input("Enter ingredient. Type 'done' when you're done: ")
        #     if ingredient.lower() == 'done':
        #         break
        #     else:
        #         self.ingredients.append(ingredient)
        # self.ingredients_string = ', '.join(self.ingredients).replace("'", "")