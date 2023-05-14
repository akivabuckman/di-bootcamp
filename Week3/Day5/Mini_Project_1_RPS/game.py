import random

class Game:
    def get_user_item(self):
        while True:
            self.user_item = input("Choose (r)ock, (p)aper, or (s)cissor: ")
            if self.user_item.lower() in "rps":
                return self.user_item


    def get_computer_item(self):
        self.computer_item = random.choice(['rock', 'paper', 'scissor'])[0]
        return self.computer_item

    def get_game_result(self):
        if self.computer_item == self.user_item:
            return "draw"
        elif (self.computer_item == 'r' and self.user_item == 'p') or \
                (self.computer_item == 'p' and self.user_item == 's') or \
                (self.computer_item == 's' and self.user_item == 'r'):
            return "win"
        else:
            return "lose"

    def play(self):
        print(f"You selected {self.get_user_item()}. Computer selected {self.get_computer_item()}. "
              f"You {self.get_game_result()}")


a = Game()
a.play()