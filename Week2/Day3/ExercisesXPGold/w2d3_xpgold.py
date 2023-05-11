def gold1():
    #Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should
    # be the person’s name, and the value should be their birthday.
    birthdays = {
        'akiva': '1991/05/02',
        'liat': '1991/12/17',
        'dani': '2017/05/03',
        'maya': '2018/09/28',
        'tali': '2021/10/08',
    }
    #Ask the user to give you a person’s name and store the answer in a variable.
    choice = input('whose bday do you want? ')
    bday = birthdays[choice]
    print(f"{choice}'s bday is {bday}")

def gold2():
    #Before asking the user to input a person’s name print out all of the names in the dictionary.
    birthdays = {
            'akiva': '1991/05/02',
            'liat': '1991/12/17',
            'dani': '2017/05/03',
            'maya': '2018/09/28',
            'tali': '2021/10/08',
    }

    for i in birthdays.keys():
        print(i)

    #If the person that the user types is not found in the dictionary, print an error message (“Sorry, we don’t have the
    # birthday information for <person’s name>”)
    choice = input('whose bday do you want? ')
    try:
        bday = birthdays[choice]
    except KeyError:
        print(f"Sorry, we don't have the birthday information for {choice}")
    else:
        print(f"{choice}'s bday is {bday}")

def gold3():
    birthdays = {
        'akiva': '1991/05/02',
        'liat': '1991/12/17',
        'dani': '2017/05/03',
        'maya': '2018/09/28',
        'tali': '2021/10/08',
    }

    # Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
    # Ask the user for a person’s name – store it in a variable.
    # Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
    # Now add this new data into your dictionary.
    user_name = input("what's your name? ")
    user_bday = input("what's your bday, in YYYY/MM/DD? ")

    birthdays[user_name] = user_bday

    for i in birthdays.keys():
        print(i)

    choice = input('whose bday do you want? ')
    try:
        bday = birthdays[choice]
    except KeyError:
        print(f"Sorry, we don't have the birthday information for {choice}")
    else:
        print(f"{choice}'s bday is {bday}")

def gold4():
    items = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    }

    #Using the dictionary above, each key-value pair represents an item and its price - print all the items and their
    # prices in a sentence.

    for k, v in items.items():
        print(f"{k}'s price is ${v}")

    #Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
    # write some code to calculate how much it would cost to buy everything in stock.
    items = {
        "banana": {"price": 4 , "stock":10},
        "apple": {"price": 2, "stock":5},
        "orange": {"price": 1.5 , "stock":24},
        "pear": {"price": 3 , "stock":1}
    }

    for k, v in items.items():
        v['buyout'] = v['price'] * v['stock']
        print(f"to buy every {k} it will cost ${v['buyout']}")