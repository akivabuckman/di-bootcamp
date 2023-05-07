# wrapper function
def run_exercise(func):
    def inner():
        print(f"{func.__name__}:")
        print(f"{func()}\n")
    return inner

# each function is a separate exercise. when main is run, all exercises will run.
@run_exercise
def xp1():
    return 'Hello world\n' * 4 + "I love python\n" *4

@run_exercise
def xp2():
    month = int(input("month? "))
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Autumn"
    elif month == 12 or 0 < month <=2:
        return "Winter"

xp2()