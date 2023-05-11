# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Use List Comprehension


words = input("words separated by commas: ")
word_list = words.split(',')  # converts to list
word_list.sort()  # alphabetizes
string = ""
for i in word_list:
    string += f"{i},"
print(string[:len(string) - 1])  # the assignment shows the output without the last comma

# i don't see where to use list comprehension here
