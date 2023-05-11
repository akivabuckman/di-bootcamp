# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True
#
# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
#
# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

import random
from w3d2_xp import Dog


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        text = ""
        for dog in args:
            text += f"{dog.name} "
        print(f"{text}all play togther")

    def do_a_trick(self):
        text_options = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        print("Not Trained" if not self.trained else f"{self.name} {random.choice(text_options)}")


pet = PetDog('petty', 1, 2)
al = Dog('al', 1, 12)
bob = Dog('bob', 12, 111)
carl = Dog('carl', 33, 122)
pet.play(al, bob, carl)
pet.do_a_trick()  # will print "Not Trained"
pet.train()
pet.do_a_trick()  # now will print a trick
