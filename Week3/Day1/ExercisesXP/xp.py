# def ninja4():
#     my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
#                sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
#                Ut enim ad minim veniam, quis nostrud exercitation ullamco
#                laboris nisi ut aliquip ex ea commodo consequat.
#                Duis aute irure dolor in reprehenderit in voluptate velit
#                esse cillum dolore eu fugiat nulla pariatur.
#                Excepteur sint occaecat cupidatat non proident,
#                sunt in culpa qui officia deserunt mollit anim id est laborum."""
#
#     print(len(my_text))
#
# def ninja5():
#     max_score = 0
#     print("Enter 'exit' to end the game")
#     while True:
#         sentence = input("Enter a sentence: ").lower()
#         if sentence.lower() == "exit":
#             break
#         elif sentence.find('a') != -1:
#             print("That has an 'a'!")
#             if max_score != 0:
#                 print(f'Current high score: {max_score}')
#             print()
#         else:
#             new_len = len(sentence)
#             if new_len < max_score:
#                 print(f'{new_len} is good but you already did better ({max_score})\n')
#             else:
#                 print(f"Great job you got {new_len} letters! That's an improvement of {new_len - max_score}!")
#                 max_score = new_len
#                 print(f'Current high score: {max_score}\n')

def run_exercise(func):
    def inner():
        print(f"{func.__name__}:")
        print(f"{func()}\n")
    return inner

@run_exercise
def xp1():
    return 'Hello world\n' * 4


@run_exercise
def xp2():
    return f"99^3*8 equals {99 ** 3 * 8}"


@run_exercise
def xp3():
    queries = ['5 < 3', '3 == 3', "3 == '3'", "'3' > 3", "'Hello' == 'hello'"]
    predictions = [False, True, False, "TypeError", False]
    values = []
    for i in queries:
        try:
            values.append(eval(i))
        except TypeError:
            values.append("TypeError")
    statement = ""
    statement += f"Predictions: {predictions}\n"
    statement += f"Values: {values}\n\n"
    if predictions == values:
        statement += "Predictions equal values"
    return statement


@run_exercise
def xp4():
    computer_brand = "lenovo"
    statement = f"I have a {computer_brand} computer"
    return statement


@run_exercise
def xp5():
    name = "akiva"
    age = 32
    shoe_size = 10.5
    info = f"my name's {name}, i'm {age} years old, and my shoe size is {shoe_size}"
    return (info)


@run_exercise
def xp6():
    a = 1
    b = 4
    if a > b:
        return "Hello World"


@run_exercise
def xp7():
    number = int(input("give a number: "))
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


@run_exercise
def xp8():
    my_name = "akiva"
    user_name = input("what's your name? ").lower()
    if my_name == user_name:
        return "wow we are the same person"
    else:
        return "oh well we're not the same person"


@run_exercise
def xp9():
    inches = float(input("what's your height in inches? "))
    cm = inches * 2.54
    if cm > 145:
        return "you're tall enough"
    else:
        return "sorry too short"

xp1()
xp2()
xp3()
xp4()
xp5()
xp6()
xp7()
xp8()
xp9()