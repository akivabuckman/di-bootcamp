import requests

EDAMAM_ID = '7c239491'
EDAMAM_KEY = 'b2450a48ca06718b544940eb54b7acc2'

class UserRecipe:
    pass

class APIRecipe:
    def __init__(self, json_data):
        print(json_data)
        self.name = json_data['recipe']['label']
        self.ingredients = json_data['recipe']['ingredientLines']

def search_all_recipes():
    valid_kw = False
    while not valid_kw:
        search_keywords = ',+'.join(input("Keywords to search (with spaces): ").split())
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
                print(search_results[view_choice - 1])
                a = APIRecipe(search_results[view_choice - 1])
                view_specific_recipe(a)
            else:
                print("Number must be 1-10!")
                continue

# print((search_all_recipes()))

def add_new_recipe():
    pass

def update_existing_recipe():
    pass

def view_favorite_recipes():
    pass

def view_specific_recipe(recipe):
    pass