import random
from hangman_art import ART

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share',
             'credit card', 'rush', 'south']
# word = random.choice(wordslist)
word = "credit card".upper()
print(word)
guessed_letters = set()
display_chars = ['_' if letter != ' ' else ' ' for letter in word]
strikes = 0
def guess_letter():
    global strikes
    choice = input("choice: ").upper()
    if choice in guessed_letters: #check if letter is already guessed
        print(f"You already guessed {choice}. Try again.")
        guessed_letters.add(choice)
        guess_letter()
    elif choice in word: #check if letter is in word
        for i in range(len(word)):
            if word[i] == choice:
                display_chars[i] = choice
        guessed_letters.add(choice)
    else:
        strikes += 1
    print(display_chars)
    print(guessed_letters)
    print(strikes)

while True:
    guess_letter()