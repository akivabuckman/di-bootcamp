import random

def challenge():
    string = input("enter string: ")
    if len(string) < 10:
        print("string not long enough\n")
    elif len(string) > 10:
        print("string too long\n")
    print(f"first character: {string[0]}")
    print(f"last character: {string[-1]}\n")
    print("unshuffled:")
    for i in range(len(string)):
        print(string[:i+1])

    # random.shuffle returns a TypeError. i'm using random.sample to convert to list of characters
    string_list = random.sample(string, len(string))
    new_string = ""
    for i in string_list:
        new_string += i
    print("\nShuffled string:")
    print(new_string)

challenge()
