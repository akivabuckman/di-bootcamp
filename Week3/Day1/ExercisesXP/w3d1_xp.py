def xp1():
    # Instantiate three Cat objects using the code provided above.
    # Outside of the class, create a function that finds the oldest cat and returns the cat.
    # Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously
    # created.

    class Cat:
        def __init__(self, cat_name, cat_age):
            self.name = cat_name
            self.age = cat_age


    cat1 = Cat('al', 1)
    cat2 = Cat('bob', 2)
    cat3 = Cat('carl', 3)

    def find_oldest(cats):
        max = 0
        for cat in cats:
            if cat.age > max:
                oldest = cat
        return oldest

    cats = [cat1, cat2, cat3]
    print(f"The oldest cat is {find_oldest(cats).name}, and is {find_oldest(cats).age} years old.")

def xp2():
    #Create a class called Dog.
    # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two
    # attributes, which values are the parameters.
    # Create a method called bark that prints the following string “<dog_name> goes woof!”.
    # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
    # Print the details of his dog (ie. name and height) and call the methods bark and jump.
    # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
    # Print the details of her dog (ie. name and height) and call the methods bark and jump.
    # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
    class Dog:
        def __init__(self, name, height):
            self.name = name
            self.height = height

        def bark(self):
            print(f"{self.name} goes woof!")

        def jump(self):
            print(f"{self.name} jumps {self.height * 2}cm high!")

    davids_dog = Dog("Rex", 50)
    print(f"David's dog is named {davids_dog.name} and is {davids_dog.height}cm tall.")
    davids_dog.bark()
    davids_dog.jump()

    sarahs_dog = Dog("Teacup", 20)
    print(f"Sarah's dog is named {sarahs_dog.name} and is {sarahs_dog.height}cm tall.")
    sarahs_dog.bark()
    sarahs_dog.jump()

    if sarahs_dog.height > davids_dog.height:
        print(sarahs_dog.name)
    else:
        print(davids_dog.name)

def xp3():
    class Song:
        def __init__(self, lyrics):
            self.lyrics = lyrics

        def sing_me_a_song(self):
            for part in self.lyrics:
                print(part)

    stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
    stairway.sing_me_a_song()

def xp4():
    class Zoo:
        def __init__(self, zoo_name):
            self.name = zoo_name
            self.animals = []

        def add_animal(self, new_animal):
            if new_animal not in self.animals:
                self.animals.append(new_animal)

        def get_animals(self):
            print(self.animals)

        def sell_animal(self, animal_sold):
            if animal_sold in self.animals:
                self.animals.remove(animal_sold)

        def sort_animals(self):
            self.animals.sort()
            self.groups = {}
            first_letters = {animal[0] for animal in self.animals}
            for index, letter in enumerate(first_letters):
                self.groups[index + 1] = [animal for animal in self.animals if animal[0] == letter]


        def get_groups(self):
            print(self.groups)

    ramat_gan_safari = Zoo("Ramat Gan Zoo")
    ramat_gan_safari.add_animal('zebra')
    ramat_gan_safari.add_animal('kangaroo')
    ramat_gan_safari.add_animal('koala')
    ramat_gan_safari.sort_animals()
    ramat_gan_safari.get_groups()
