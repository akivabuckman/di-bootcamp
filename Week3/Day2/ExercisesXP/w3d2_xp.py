def xp1():
    class Pets():
        def __init__(self, animals):
            self.animals = animals

        def walk(self):
            for animal in self.animals:
                print(animal.walk())

    class Cat():
        is_lazy = True

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def walk(self):
            return f'{self.name} is just walking around'

    class Bengal(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    class Chartreux(Cat):
        def sing(self, sounds):
            return f'{sounds}'

    class Siamese(Cat):
        pass

    cat1 = Bengal('al', 1)
    cat2 = Chartreux('bob', 2)
    cat3 = Siamese('carl', 3)

    all_cats = [cat1, cat2, cat3]

    sara_pets = Pets(all_cats)

    sara_pets.walk()

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self. age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, opponent):
        if self.run_speed() > opponent.run_speed():
            print(f"{self.name} wins!")
        else:
            print(f"{opponent.name} wins!")

al = Dog('al', 1, 12)
bob = Dog('bob', 12, 111)
carl = Dog('carl', 33, 122)
dogs = [al, bob, carl]
for dog in dogs:
    dog.bark()
    dog.run_speed()
    dog.fight(dogs)