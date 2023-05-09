def challenge1():
    # Ask a user for a word
    word = list(input("word: "))
    print(word)

    # Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
    dictionary = {}
    for check_letter in word:
        indices = []
        for index, letter in enumerate(word):
            indices = [index for index, letter in enumerate(word) if letter == check_letter]
        dictionary[check_letter] = indices

    print(dictionary)


#Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20",
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2",
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200",
}

wallet = float(input("wallet: $"))
affordable = []
# clean the money data in dictionary
for k, v in items_purchase.items():
    v = float(v.replace('$','').replace(',','')) #removes $ and , and makes it a float instead of string
    items_purchase[k] = v #replaces the dirty values with clean ones
    if wallet >= v:
        affordable.append(k)
if affordable:
    print(affordable)

    #Sort the list in alphabetical order.
    affordable.sort()
    print(affordable)

else:
    print("Nothing")

#Return “Nothing” if you can’t afford anything from the store.
#in the code above in if/else