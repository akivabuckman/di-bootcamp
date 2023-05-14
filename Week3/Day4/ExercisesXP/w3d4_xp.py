#🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long
# the sentence should be and then printing the generated sentence.
#
# Hint : The generated sentences do not have to make sense.
#
# Download this word list
#
# Save it in your development directory.
#
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a
# collection. What is the correct data type to store the words?
#
# Create another function called get_random_sentence which takes a single parameter called length. The length parameter
# will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
#
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
#
# Create a function called main which will:
#
# Print a message explaining what the program does.
#
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your
# data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
def xp1():
    import random

    def get_words_from_file(file):
        with open (file, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def get_random_sentence(length):
        word_bank = get_words_from_file("sowpods.txt")
        words = [random.choice(word_bank).lower() for i in range(length)]
        return ' '.join(words)

    def get_length():
        length = input('Choose sentence length between 2-20: ')
        try:
            length = int(length)
        except ValueError:
            print('Choose between 2 and 20!')
            quit()
        else:
            if not 2 <= length <= 20:
                print('Choose between 2 and 20!')
                quit()
            else:
                return get_random_sentence(length)


    def main():
        print("The program takes a user-defined sentence word length, and returns a sentence of that length of random "
              "words.")
        get_length()

    main()


#🌟 Exercise 2: Working With JSON
# Instructions
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
#
#
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

def xp2():
    import json
    sampleJson = """{ 
       "company":{ 
          "employee":{ 
             "name":"emma",
             "payable":{ 
                "salary":7000,
                "bonus":800
             }
          }
       }
    }"""

    new_dict = json.loads(sampleJson)
    new_dict['company']['employee']['birth_date'] = None
    with open('new_file', 'w') as file:
        file.write(str(new_dict))