import string


sample = "A good bo$ok would sometimes cost as much as a good house."

class Text:
    def __init__(self, string):
        self.text = string

    def word_count(self, word):
        self.count = self.text.count(word)
        self.word_list = self.text.split(' ')
        return max(set(self.word_list), key=self.word_list.count)

    def unique_words(self):
        return list(set(self.word_list))

    @classmethod
    def from_file(cls, file):
        with open(file, 'r') as file:
            file_text = file.readlines()
            return Text(file_text)

class TextModification(Text):
    def depunctuate(self):
        self.text = self.text.translate(str.maketrans('', '', string.punctuation))
        return self

    def no_stops(self):
        with open('stopwords.txt', 'r') as stop_file:
            SW = stop_file.readlines()
            STOP_WORDS = [i.strip() for i in SW]
        stopless_list = [i for i in self.text.split(' ') if i.lower() not in STOP_WORDS]
        self.text = ' '.join(stopless_list)
        return self

    def no_specials(self):
        string = ""
        for char in self.text:
            if char == ' ':
                string += ' '
            elif char.isalnum():
                string += char
        self.text = string
        return self
