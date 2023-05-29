import requests
import psycopg2
import smtplib
import tkinter as tk

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='hackathon1')
CURSOR = CONNECTION.cursor()
EDAMAM_ID = '7c239491'
EDAMAM_KEY = 'b2450a48ca06718b544940eb54b7acc2'

class Recipe:
    def add_recipe_to_favorites(self, active_user, input_type):
        CURSOR.execute(f"SELECT recipe_name FROM favorites "  # finds user's favorites' names
                       f"INNER JOIN user_favorites ON user_favorites.recipe_id = favorites.recipe_id "
                       f"INNER JOIN users ON user_favorites.user_id = users.user_id AND users.username "
                       f"ILIKE '{active_user}';")
        # existing_faves = [i[0] for i in CURSOR.fetchall()] # not needed. users can have duplicate favorite names.
        # if self.name in existing_faves:
        #     if input_type == 'api':
        #         print(f"A favorite named {self.name} already exists. Pick another action.")
        #     elif input_type == 'user':
        #         print(f"A favorite named {self.name} already exists. Use a different name.")
        #         create_user_recipe(active_user)
        # else:
        CURSOR.execute(f"INSERT INTO favorites(recipe_name, ingredients, cook_time, cuisine, diet_code) VALUES"
                       f"('{self.name}', '{self.ingredients_string}', '{self.cook_time}', '{self.cuisine}', "
                       f"'{self.diet_code}');")
        CONNECTION.commit()
        CURSOR.execute(f"INSERT INTO user_favorites(user_id, recipe_id) VALUES"
                       f"((SELECT user_id FROM users WHERE username ILIKE '{active_user}'),"
                       f"(SELECT recipe_id FROM favorites WHERE recipe_id = "
                       f"(SELECT MAX(recipe_id) FROM favorites)))")
        CONNECTION.commit()
        print(f"\n{self.name} added to Favorites")


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


class UserRecipe(Recipe):
    def __init__(self):
        # input of new recipe details
        self.name = input("\nRecipe Name: ").replace("'", '').title()
        while True:
            self.cook_time = input("Cook time [min]: ")
            try:
                self.cook_time = int(self.cook_time)
            except ValueError:
                print("Enter an integer!")
                continue
            else:
                break
        self.cuisine = input("Cuisine: ").replace("'", "")
        while True:
            self.diet_code = input("Enter diet code. 0: None, 1: Vegetarian, 2: Vegan, 3: Celiac ")
            if self.diet_code not in ['0', '1', '2', '3']:
                print("Choose 0, 1, 2, or 3!")
                continue
            else:
                break
        # ingredient entry:
        self.ingredients = []
        done = False
        while not done:
            ingredient = input("Enter ingredient. Type 'done' when you're done: ")
            if ingredient.lower() == 'done':
                break
            else:
                self.ingredients.append(ingredient)
        self.ingredients_string = ', '.join(self.ingredients).replace("'", "")