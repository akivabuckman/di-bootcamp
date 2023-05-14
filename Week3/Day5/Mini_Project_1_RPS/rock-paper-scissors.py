import game as gm
def get_user_menu_choice():
    print("Menu:\n(g) Play a new game\n(s) Show scores\n(q) Quit")
    return input("What do you choose to do? ")

def print_results(results):
    print(f"Wins: {results['win']}\nLosses: {results['lose']}\nDraws: {results['draw']}\n\n")


results = {'win':0, 'lose':0, 'draw':0}

def main():
    chosen = False
    while not chosen:
        menu_choice = get_user_menu_choice().lower()
        chosen = True if menu_choice in "gsq" else False
    if menu_choice == 'g':
        game = gm.Game()
        results[game.play()] += 1
        main()
    elif menu_choice == 's':
        print_results(results)
        main()
    elif menu_choice == 'q':
        pass
main()