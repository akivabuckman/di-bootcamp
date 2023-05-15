class AnagramChecker:
    def __init__(self):
        with open('sowpods.txt', 'r') as file:
            self.word_bank = [i.strip() for i in file.readlines()]  # word file into list

    def is_valid_word(self, word):
        self.word = word.upper().strip()
        self.word_count = len(self.word.split(' '))
        self.alpha = False if any(not letter.isalpha() for letter in self.word) else True  # false if any non-alpha
        self.real = True if self.word.upper() in self.word_bank else False  # false if not in word bank
        return True if self.real == True and self.alpha == True else False

    def get_anagrams(self):
        self.letters = [i for i in self.word]  # list of letters in given word
        self.anagrams = [word for word in self.word_bank if sorted(word) == sorted(self.word)]  # list of anagrams
        self.anagrams.remove(self.word)  # remove the word itself
        return self.anagrams
