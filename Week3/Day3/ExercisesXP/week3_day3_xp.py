def xp1():
    print("xp1:")
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    result = dict(zip(keys, values,))
    print(result)

def xp2():
    print("xp2:")
    family = {}
    while True:
        info = input("enter name and age. type 'done' when done: ").split()
        if info[0] == "done":
            break
        new_name = info[0]
        new_age = int(info[1])
        family[new_name] = new_age
    prices = {}
    total = 0
    for key, value in family.items():
        if value < 3:
            prices[key] = 0
        elif 3 <= value <=12:
            prices[key] = 10
        else:
            prices[key] = 15
        print(f"{key}: ${prices[key]}")
        total += prices[key]

    print(f"Total: ${total}")

def xp3():
    print("xp3:")
    info = {
        'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': 'men, women, children, home',
        'international_competitors': ['Gap','H&M','Benetton'],
        'number_stores': 7000,
        'major_color': {
            'France': 'blue',
            'Spain': 'red',
            'US': 'pink, green',
        }
    }

    # 3. Change the number of stores to 2.
    info['number_stores'] = 2

    #4. Print a sentence that explains who Zaras clients are.
    print(f"Zara's clients are {info['type_of_clothes']}")

    #5. Add a key called country_creation with a value of Spain.
    info['country_creation'] = 'Spain'
    print(f"Spain added as country_cration: {info}")

    # 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
    for key in info.keys():
        if key == "international_competitors":
            info[key].append("Desigual")
    print(f"Desigual added to internation competitors: {info}")

    #7. Delete the information about the date of creation.
    info.pop('creation_date')
    print(f"creation date removed: {info}")

    #8. Print the last international competitor.
    print(f"last international competitor: {info['international_competitors'][-1]}")

    #9. Print the major clothes colors in the US.
    print(f"major US colors: {info['major_color']['US']}")

    #10. Print the amount of key value pairs (ie. length of the dictionary).
    print(f"amount of key/value pairs: {len(info)}")

    #11. Print the keys of the dictionary.
    print(f"keys: {info.keys()}")

    #12. Create another dictionary called more_on_zara with the following details:
    more_on_zara = {
        'creation_date': 1975,
        'number_stores': 10000,
    }

    #13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
    for key, value in more_on_zara.items():
        info[key] = value
    print(f"more info added: {info}")

    #14. Print the value of the key number_stores. What just happened ?
    print(f"each dictionary only has one item per key. in the previous step we made number of stores 10,000, which replaced"
          f" the previous value.\n"
          f"number_stores: {info['number_stores']}")

print("xp4:")
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# #1/
#
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
# #2/
#
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# #3/
#
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
disney_users_A = {}
for index, item in enumerate(users):
    disney_users_A[item] = index
print(f'A: {disney_users_A}')

disney_users_B = {}
for index, item in enumerate(users):
    disney_users_B[index] = item
print(f"B: {disney_users_B}")

disney_users_C = {}
for index,item in enumerate(sorted(users)):
    disney_users_C[item] = index
print(f"C: {disney_users_C}")

# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
disney_users_A = {}
for index, item in enumerate(users):
    if 'i' in item:
        disney_users_A[item] = index
print(f'A: {disney_users_A}')

# Only recreate the 1st result for:
# The characters, which names start with the letter “m” or “p”.
disney_users_A = {}
for index, item in enumerate(users):
    print(index, item)
    if item[0] == 'M' or item[0] == 'P':
        disney_users_A[item] = index
print(f'A: {disney_users_A}')