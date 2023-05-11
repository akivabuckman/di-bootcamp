class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal, amount=1):
        for i in range(amount):
            self.animals.append(animal)

    def get_info(self):
        statement = f"{self.name}'s farm\n\n"
        for i in set(self.animals):
            statement += f"{i} : {self.animals.count(i)}\n"
        statement += "\n    E-I-E-I-O!"
        return statement

    def get_animal_types(self):
        self.types = list(set(self.animals))
        self.types.sort()
        return self.types

    def get_short_info(self):
        types = self.get_animal_types()
        statement = f"{self.name}'s farm has "
        for i in range(len(types)):
            if i == len(types) - 1:
                statement += f"and {types[i]}s."
            else:
                statement += f"{types[i]}s, "
        return statement

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
macdonald.get_animal_types()
print(macdonald.get_short_info())
# McDonald's farm
#
# cow : 5
# sheep : 2
# goat : 12
#
#     E-I-E-I-0!