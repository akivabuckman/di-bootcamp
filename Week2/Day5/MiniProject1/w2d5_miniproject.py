import numpy as np

spaces = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def player_turn(player):
    print(f"{player.upper()} Player's turn...")
    row = int(input("Enter row 1-3: ")) - 1
    column = int(input("Enter column 1-3: ")) - 1
    if not 0 <= row <= 2 or not 0 <= column <= 2:
        print("\nYou gotta pick 1-3 buddy.")
        display()
        player_turn(player)

    elif spaces[row][column] != ' ':
        print("\nThat space is already taken!")
        display()
        player_turn(player)
    else:
        spaces[row][column] = player


def check(player):
    transposed = np.rot90(spaces)  # do this so the same function can check all rows, cols, and diags in one loop
    for array in [spaces, transposed]:
        for row in array:  # so that we check the rows and diagonal, then rotates 90 degrees and does the same
            if all(space == player for space in row):  # checks rows and columns
                print(f"{player.upper()} wins!")
                quit()
            if all(array[i][i] == player for i in range(3)):  # checks diagonal
                print(f"{player.upper()} wins!")
                quit()
        if all(all(space != ' ' for space in row) for row in array):  # checks for tie, if there are no ' 's
            print(f"Tie!")
            quit()


def display():
    LINE = "*****************"
    GRID = "*  ---|---|---  *"
    DISPLAY_ROWS = [f"*   {row[0]} | {row[1]} | {row[2]}   *" for row in spaces]
    print("\nTIC    TAC    TOE")
    print(LINE)
    print(DISPLAY_ROWS[0])
    print(GRID)
    print(DISPLAY_ROWS[1])
    print(GRID)
    print(DISPLAY_ROWS[2])
    print(LINE)

def play():
    display()
    while True:
        for player in ['x', 'o']:
            player_turn(player)
            display()
            check(player)

play()