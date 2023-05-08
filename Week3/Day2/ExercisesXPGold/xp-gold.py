def xp1():
    list1 = [1,2,3]
    list2= [4,5,6]
    for i in list1:
        list2.append(i)
    print(list2)

def xp2():
    for i in range(1500,2500):
        if i % 5 == 0 or i % 7 == 0:
            print(i)

def xp3():
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
    user = input("name: ")
    if user in names:
        print(names.index(user))

def xp4():
    print("Test Data")
    first = int(input("Input the 1st number: "))
    second = int(input("Input the 2nd number: "))
    third = int(input("Input the 3rd number: "))
    print(f"The greatest number is: {max(first, second, third)}")

def xp5():
    letters = list("abcdefghijklmnopqrstuvwxyz")
    vowels = list("aeiou")
    consonants = [i for i in letters if i not in vowels]
    for i in letters:
        if i in vowels:
            print(f"{i} is a vowel")
        else:
            print(f"{i} is a consonant")

def xp6():
    words = input("type 7 words separated by space: ").split(' ')
    letter = input("choose letter: ")
    for i in words:
        print(i.index(letter))

