def dc1():
    pass
    # 1. A class is an object creator, that provides an outline for what an object should do and what attributes it should have
    # 2. An instance is an object created through the class
    # 3. Encapsulation is hiding an object's data from other classes, so that it's only accessible through its own class
    # 4. Abstraction is a process that hides information from the user, usually the internal details of a function
    # 5. Inheritance is where a class inherits attributes and/or functions from a parent class
    # 6. Multiple inheritance is where a class inherits attributes from more than one parent class
    # 7. Polymorphism is where different object types behave differently to a function/attribute
    # 8. MRO is the order in which a method is activated throughout multiple classes


def dc2():
    import random

    class Deck:
        def __init__(self):
            self.cards = []

        def shuffle(self):
            if len(self.cards) == 52:
                random.shuffle(self.cards)
            print(self.cards)

        def deal(self):
            choice = random.choice(self.cards)
            self.cards.remove(choice)
            return choice

    class Card:
        def __init__(self, suit, value):
            self.suit = suit
            self.value = value

    SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
    VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    deck = Deck()
    for suit in SUITS:
        for value in VALUES:
            a = Card(suit, value)
            deck.cards.append(a)