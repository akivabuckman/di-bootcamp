# wrapper function
def run_exercise(func):
    def inner():
        print(f"{func.__name__}:")
        print(f"{func()}\n")
    return inner

# each function is a separate exercise. when main is run, all exercises will run.
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
    statement = f"Queries: {queries}\n"
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