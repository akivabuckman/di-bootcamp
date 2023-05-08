import random


def xp1():
    faves = {0, 2, 4}
    for i in range(2):
        faves.add(random.randint(5,55)) #add 2 random numbers to the set
    print(f"added 2 numbers: {faves}")
    fave_list = list(faves) #convert to list so it's indexed
    fave_list.pop()
    print(f"with last item removed: {fave_list}")
    friend_fav_numbers = {1, 2, 3}
    our_fav_numbers = faves.union(friend_fav_numbers)
    print(f"me and friend: {our_fav_numbers}")

def xp2():
    # No you can't add more integers to a tuple. They're immutable.
    pass

def xp3():
    basket = ["Banana", "Apples", "Oranges", "Blueberries"]
    basket.remove("Banana")
    basket.remove("Blueberries")
    basket.append("Kiwi")
    basket.insert(0, "Apples")
    apple_count = len([i for i in basket if i=="Apples"]) #creates a list of all instances of "Apple" then calculates len
    basket.clear()
    print(basket)

def xp4():
    # 1. floats have numbers after the decimals. integers don't.
    # 2. random module
    # 3.
    my_list = [i / 2 for i in range(3, 11)]
    for i, item in enumerate(my_list):
        if item % 1 == 0:
            my_list[i] = int(item)
    print(my_list)


def xp5():
    for i in range(1,21): #print all 1-20
        print(i)

    for i in range(1,21): #print even 1-20
        if i % 2 == 0:
            print(i)

def xp6():
    while True:
        my_name = "akiva"
        name = input("name? ").lower()
        if my_name == name:
            break

def xp7():
    fruits = input("tell me your favorite fruits, with spaces: ").split(' ')
    choice = input("pick a fruit: ").lower()
    if choice in fruits:
        print("You chose one of your favorite fruits! Enjoy!")
    else:
        print("You chose a new fruit. I hope you enjoy")

def xp8():
    toppings = []
    total = 10
    while True:
        choice = input("enter topping: ").lower()
        if choice == "quit":
            break
        toppings.append(choice)
        print(f"ok i'll add some {choice}\n")
        total += 2.5
    topping_string = ""
    for i in toppings:
        topping_string += f"{i} "
    print(f"enjoy your pizza with {topping_string}")
    print(f"your total is ${'{:.2f}'.format(total)}")

def xp9a():
    ages = input("enter all ages divided by a space: ").split(' ')
    ages_int = [int(item) for i, item in enumerate(ages)]
    total = 0
    for i in ages_int:
        if 3 <= i <= 12:
            total += 10
        elif 12 < i:
            total += 15

    print(f"total cost: ${'{:.2f}'.format(total)}")

def xp9b():
    names = ["al", "bob", "cathy", "drew", "ellen"]
    for i in names:
        age = int(input(f"what is {i}'s age? "))
        if 16 < age < 21:
            names.remove(i)
    print(names)

def xp10():
    sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
    finished_sandwiches = []
    #it's unclear how to "make" a sandwich... i will do it like this:
    while len(sandwich_orders) > 0:
        print()
        for count, value in enumerate(sandwich_orders):
            print(f"{count}: {value}")
        choice = int(input("choose an index to 'make' a sandwich: "))
        print(f"\ni made your {sandwich_orders[choice]}")
        finished_sandwiches.append(sandwich_orders[choice])
        sandwich_orders.remove(sandwich_orders[choice])
        print(f"finished sandwiches: {finished_sandwiches}")

def xp11():
    sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
    for i in range(3): #adds 3 pastrami sandwiches
        sandwich_orders.append("Pastrami sandwich")
    print("deli is out of pastrami")
    pastrami_count = 0
    for i in sandwich_orders:
        if i == "Pastrami sandwich":
            pastrami_count += 1
    while pastrami_count > 0: #removes all pastrami sandwiches
        sandwich_orders.remove("Pastrami sandwich")
        pastrami_count -= 1
    finished_sandwiches = []
    #it's unclear how to "make" a sandwich... i will do it like this:
    while len(sandwich_orders) > 0:
        print()
        for count, value in enumerate(sandwich_orders):
            print(f"{count}: {value}")
        choice = int(input("choose an index to 'make' a sandwich: "))
        print(f"\ni made your {sandwich_orders[choice]}")
        finished_sandwiches.append(sandwich_orders[choice])
        sandwich_orders.remove(sandwich_orders[choice])
    print(f"finished sandwiches: {finished_sandwiches}")

xp10()