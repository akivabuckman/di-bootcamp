# wrapper function
def run_exercise(func):
    def inner():
        print(f"{func.__name__}:")
        print(f"{func()}\n")

    return inner


# each function is a separate exercise. when main is run, all exercises will run.
@run_exercise
def ninja4():
    my_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
               sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
               Ut enim ad minim veniam, quis nostrud exercitation ullamco
               laboris nisi ut aliquip ex ea commodo consequat.
               Duis aute irure dolor in reprehenderit in voluptate velit
               esse cillum dolore eu fugiat nulla pariatur.
               Excepteur sint occaecat cupidatat non proident,
               sunt in culpa qui officia deserunt mollit anim id est laborum."""

    return f"the text has {len(my_text)} letters."

@run_exercise
def ninja5():
    max_score = 0
    print("Enter 'exit' to end the game")
    while True:
        sentence = input("Enter a sentence: ").lower()
        if sentence.lower() == "exit":
            break
        elif sentence.find('a') != -1:
            print("That has an 'a'!")
            if max_score != 0:
                print(f'Current high score: {max_score}')
            print()
        else:
            new_len = len(sentence)
            if new_len < max_score:
                print(f'{new_len} is good but you already did better ({max_score})\n')
            else:
                print(f"Great job you got {new_len} letters! That's an improvement of {new_len - max_score}!")
                max_score = new_len
                print(f'Current high score: {max_score}\n')


def ninja3():

    queries = ["3 <= 3 < 9", "3 == 3 == 3"]
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