import requests
import psycopg2
import smtplib

CONNECTION = psycopg2.connect(host='localhost', user='postgres', password='1234', dbname='hackathon1')
CURSOR = CONNECTION.cursor()
EDAMAM_ID = '7c239491'
EDAMAM_KEY = 'b2450a48ca06718b544940eb54b7acc2'


class Recipe:
    def add_recipe_to_favorites(self, active_user):
        CURSOR.execute(f"INSERT INTO favorites(recipe_name, ingredients, cook_time, cuisine, diet_code) VALUES"
                       f"('{self.name}', '{self.ingredients_string}', '{self.cook_time}', '{self.cuisine}', "
                       f"'{self.diet_code}');")
        CONNECTION.commit()
        CURSOR.execute(f"INSERT INTO user_favorites(user_id, recipe_id) VALUES"
                       f"((SELECT user_id FROM users WHERE username = '{active_user}'),"
                       f"(SELECT recipe_id FROM favorites WHERE recipe_name = '{self.name}'))")
        CONNECTION.commit()
        print(f"{self.name} added to Favorites")

    def email_recipe(self, active_user):
        SENDER = 'akivabuckman@gmail.com'
        RECEIVER = 'akivabuckman@gmail.com'


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


# def search_all_recipes():
#     valid_kw = False
#     while not valid_kw:
#         search_keywords = ',+'.join(input("\nKeywords to search (with spaces): ").split())
#         if search_keywords != '':
#             break
#     cuisine_input = input('Enter cuisine: ')
#     cuisine = f"&cuisineType={cuisine_input}" if cuisine_input != '' else ''
#     diet_input = input('Enter diet restriction: ')
#     diet = f"&cuisineType={diet_input}" if diet_input != '' else ''
#     URL = f'https://api.edamam.com/search?q={search_keywords}&app_id={EDAMAM_ID}&app_key={EDAMAM_KEY}{diet}{cuisine}'
#     search_results = requests.get(url=URL).json()['hits']
#     titles = [i['recipe']['label'] for i in search_results]
#     if len(titles) == 0:
#         print("No results. Search again.")
#         search_all_recipes()
#     enum = enumerate(titles)
#     for count, value in enum:
#         print(f"{count + 1}.", value)
#     while True:
#         view_choice = input("Which # recipe would you like to view? (1-10): ")
#         try:
#             view_choice = int(view_choice)
#         except ValueError:
#             print("Pick a number!")
#             continue
#         else:
#             if 1 <= view_choice <= 10:
#                 # print(search_results[view_choice - 1])
#                 a = APIRecipe(search_results[view_choice - 1])
#                 view_specific_recipe(a)
#                 return
#             else:
#                 print("Number must be 1-10!")
#                 continue

def get_search_parameters(active_user):
    params = {}
    valid_kw = False
    while not valid_kw:
        search_keywords = ',+'.join(input("\nKeywords to search (with spaces): ").split())
        if search_keywords != '':
            break
    cuisine_input = input('Enter cuisine: ')
    cuisine = f"&cuisineType={cuisine_input}" if cuisine_input != '' else ''
    diet_input = input('Enter diet restriction: ')
    diet = f"&cuisineType={diet_input}" if diet_input != '' else ''
    params['search_keywords'] = search_keywords
    params['diet'] = diet
    params['cuisine'] = cuisine
    search_all_recipes(params, active_user)


def search_all_recipes(params, active_user):
    URL = f"https://api.edamam.com/search?q={params['search_keywords']}&app_id={EDAMAM_ID}&app_key={EDAMAM_KEY}" \
          f"{params['diet']}{params['cuisine']}"
    search_results = requests.get(url=URL).json()['hits']
    titles = [i['recipe']['label'] for i in search_results]
    if len(titles) == 0:
        print("No results. Search again.")
        get_search_parameters(active_user)
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
                a = APIRecipe(search_results[view_choice - 1])
                view_specific_recipe(a, params, active_user)
                return
            else:
                print("Number must be 1-10!")
                continue


def view_favorite_recipes(active_user):
    CURSOR.execute("SELECT * FROM favorites")
    recipe_response = CURSOR.fetchall()
    print(recipe_response)


def view_specific_recipe(recipe, params, active_user):
    CURSOR.execute(f"SELECT diet_name FROM diets WHERE diet_code = {recipe.diet_code}")  # converts API's diet info
    diet_type = CURSOR.fetchall()[0][0]
    print(f"\n{recipe.name}")
    print(f"Cuisine: {recipe.cuisine.title()}")
    print(f"Diet Type: {diet_type}")
    ingredients_print = recipe.ingredients_string.replace('\n', ", ")
    print(f"\nIngredients:\n{ingredients_print}")
    while True:
        recipe_view_choice = input("\nWhat would you like to do?\n(E)mail recipe\n(A)dd to favorites\n"
                                   "Back to search (R)esults\n(H)ome: ")
        if recipe_view_choice.lower() == 'a':
            recipe.add_recipe_to_favorites(active_user)
        elif recipe_view_choice.lower() == 'e':
            recipe.email_recipe(active_user)
        elif recipe_view_choice.lower() == 'r':
            search_all_recipes(params, active_user)
        elif recipe_view_choice.lower() == 'h':
            break

def create_user_recipe(active_user):
    ur = UserRecipe()
    ur.add_recipe_to_favorites()