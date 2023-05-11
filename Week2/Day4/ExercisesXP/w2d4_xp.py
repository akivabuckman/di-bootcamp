import random


def xp1():
    # Write a function called display_message() that prints one sentence telling everyone what you are learning in this
    # course.
    def display_message():
        print("we're learning full stack")

    # Call the function, and make sure the message displays correctly.
    display_message()


def xp2():
    # Write a function called favorite_book() that accepts one parameter called title.
    # The function should print a message, such as "One of my favorite books is <title>".
    # Call the function, make sure to include a book title as an argument when calling the function.
    def favorite_book(title):
        print(f"one of my favorite books is {title}")

    favorite_book("DI Handbook")


def xp3():
    # Write a function called describe_city() that accepts the name of a city and its country as parameters.
    # The function should print a simple sentence, such as "<city> is in <country>".
    # For example “Reykjavik is in Iceland”
    # Give the country parameter a default value.
    # Call your function.
    def describe_city(city, country="Israel"):
        print(f"{city.title()} is in {country.title()}")

    describe_city("paris", "france")


def xp4():
    # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
    # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and
    # display both numbers.
    def compare(number):
        random_number = random.randint(1, 100)
        if random_number == number:
            print("success")
        else:
            print(f"fail. {number} and {random_number} aren't the same.")

    compare(input("select random number: "))


def xp5():
    # Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
    # The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The
    # size of the shirt is <size> and the text is <text>"
    # Call the function make_shirt().
    #
    # Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by
    # default.
    # Make a large shirt with the default message
    # Make medium shirt with the default message
    # Make a shirt of any size with a different message.
    #
    # Bonus: Call the function make_shirt() using keyword arguments.
    def make_shirt_1(size, text):
        print(f"The size of the shirt is {size} and the text is '{text}'")

    make_shirt_1("small", "i ❤️DI")

    def make_shirt_2(size="large", text="I love Python"):
        print(f"The size of the shirt is {size} and the text is '{text}'")

    make_shirt_2()  # default
    make_shirt_2(size="medium")  # medium, default text
    make_shirt_2(size="small", text="i love functions")  # no default


def xp6():
    # Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
    # Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
    # Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great"
    # to each magician’s name.
    # Call the function make_great().
    # Call the function show_magicians() to see that the list has actually been modified.
    magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

    def show_magicians(magicians):
        for i in magicians:
            print(i)

    show_magicians(magician_names)

    def make_great(magicians):
        for i in range(len(magicians)):
            magicians[i] = f"{magicians[i]} the Great"

    make_great(magician_names)
    show_magicians(magician_names)


def xp7():
    # Create a function called get_random_temp().
    # This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
    # Test your function to make sure it generates expected results.
    #
    # Create a function called main().
    # Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
    # Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
    #
    # Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
    # below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
    # between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
    # between 16 and 23
    # between 24 and 32
    # between 32 and 40
    #
    # Change the get_random_temp() function:
    # Add a parameter to the function, named ‘season’.
    # Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits
    # based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
    # Now that we’ve changed get_random_temp(), let’s change the main() function:
    # Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly.
    # Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
    # Use the season as an argument when calling get_random_temp().
    #
    # Bonus: Give the temperature as a floating-point number instead of an integer.
    # Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December).
    # Determine the season according to the month.
    def get_random_temp1():
        return random.randint(-10, 40)

    def main():
        celsius = get_random_temp1()
        print(f"The temperature right now is {celsius} degrees Celsius.")
        if celsius < 0:
            print("Brrr, that’s freezing! Wear some extra layers today")
        elif celsius < 16:
            print("Quite chilly! Don't forger your coat")
        elif celsius < 23:
            print("Enjoy the nice weather")
        elif celsius < 32:
            print("The summer is coming")
        elif celsius < 40:
            print("Isn't Israel's weather the greatest?")

    main()

    def get_random_temp2(month):
        if month in [12, 1, 2]:
            return round(random.uniform(-10, 0), 1)
        elif 3 <= month <= 5 or 9 <= month <= 11:
            return round(random.uniform(0, 25), 1)
        else:
            return round(random.uniform(25, 40), 1)

    def main2():
        celsius = get_random_temp2(float(input("select month (1-12): ")))
        print(f"The temperature right now is {celsius} degrees Celsius.")
        if celsius < 0:
            print("Brrr, that’s freezing! Wear some extra layers today")
        elif celsius < 16:
            print("Quite chilly! Don't forger your coat")
        elif celsius < 23:
            print("Enjoy the nice weather")
        elif celsius < 32:
            print("The summer is coming")
        elif celsius < 40:
            print("Isn't Israel's weather the greatest?")

    main2()
