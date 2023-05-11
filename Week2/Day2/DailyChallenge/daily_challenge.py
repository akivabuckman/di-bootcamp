def challenge1():
    choices = input("choose a number and length, separate by space: ").split(' ')
    number = int(choices[0])
    length = int(choices[1])
    numlist = [(i + 1) * number for i in range(length)]
    print(numlist)

def challenge2():
    word = input("choose a word: ")
    previous = ""
    final = ""
    for i in word:
        if i != previous:
            final += i
        previous = i
    print(final)