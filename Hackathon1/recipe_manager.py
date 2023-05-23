import requests
import psycopg2
import smtplib

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='hackathon1')
CURSOR = CONNECTION.cursor()
EDAMAM_ID = '7c239491'
EDAMAM_KEY = 'b2450a48ca06718b544940eb54b7acc2'

class Recipe:
    def add_new_recipe(self):
        print(self.ingredients_string)
        CURSOR.execute(f"INSERT INTO favorites(recipe_name, ingredients, cook_time, cuisine, diet_code) VALUES"
                       f"('{self.name}', '{self.ingredients_string}', '{self.cook_time}', '{self.cuisine}', "
                       f"'{self.diet_code}');")
        CONNECTION.commit()

    def update_existing_recipe(self):
        pass

    def email_recipe(self):
        SENDER = 'akivabuckman@gmail.com'
        RECEIVER = 'akivabuckman@gmail.com'


class APIRecipe(Recipe):
    def __init__(self, json_data):
        self.name = json_data['recipe']['label']
        self.ingredients = json_data['recipe']['ingredientLines']
        self.ingredients_string = '\n'.join(self.ingredients)
        self.cook_time = int(json_data['recipe']['totalTime'])
        self.cuisine = json_data['recipe']['cuisineType'][0]
        self.diet_code = 3 if 'Celiac' in json_data['recipe']['healthLabels'] else \
            2 if 'Vegan' in json_data['recipe']['healthLabels'] else \
                1 if 'Vegetarian' in json_data['recipe']['healthLabels'] else 0


class UserRecipe(Recipe):
    pass


def search_all_recipes():
    valid_kw = False
    while not valid_kw:
        search_keywords = ',+'.join(input("\nKeywords to search (with spaces): ").split())
        if search_keywords != '':
            break
    cuisine_input = input('Enter cuisine: ')
    cuisine = f"&cuisineType={cuisine_input}" if cuisine_input != '' else ''
    diet_input = input('Enter diet restriction: ')
    diet = f"&cuisineType={diet_input}" if diet_input != '' else ''
    URL = f'https://api.edamam.com/search?q={search_keywords}&app_id={EDAMAM_ID}&app_key={EDAMAM_KEY}{diet}{cuisine}'
    search_results = requests.get(url=URL).json()['hits']
    titles = [i['recipe']['label'] for i in search_results]
    if len(titles) == 0:
        print("No results. Search again.")
        search_all_recipes()
    enum = enumerate(titles)
    for count, value in enum:
        print(f"{count + 1}.", value)
    while True:
        view_choice = input("Which # recipe would you like to view? (1-10): ")
        try:
            view_choice = int(view_choice)
        except ValueError:
            print("Pick a number!")
            continue
        else:
            if 1 <= view_choice <= 10:
                # print(search_results[view_choice - 1])
                a = APIRecipe(search_results[view_choice - 1])
                view_specific_recipe(a)
                return
            else:
                print("Number must be 1-10!")
                continue


def view_favorite_recipes():
    pass


def view_specific_recipe(recipe):
    CURSOR.execute(f"SELECT diet_name FROM diets WHERE diet_code = {recipe.diet_code}") # converts API's diet info
    diet_type = CURSOR.fetchall()[0][0]
    print(f"\n{recipe.name}")
    print(f"Cuisine: {recipe.cuisine.title()}")
    print(f"Diet Type: {diet_type}")
    print(f"\nIngredients:\n{recipe.ingredients_string}")
    while True:
        recipe_view_choice = input("What would you like to do?\n(E)mail recipe\n(A)dd to favorites\n"
                                   "(B)ack to search results: ")
        if recipe_view_choice.lower() == 'a':
            recipe.add_new_recipe()
        elif recipe_view_choice.lower() == 'e':
            recipe.email_recipe()
        elif recipe_view_choice.lower() == 'b':
            
