import anagram_checker


def get_user_menu_choice():
    print("\nMenu:\n(w) Check word\n(q) Quit")
    return input("What do you choose to do? ")


def main():
    chosen = False
    while not chosen:
        menu_choice = get_user_menu_choice().lower()
        chosen = True if menu_choice in "qw" else False
    if menu_choice == 'w':
        a = anagram_checker.AnagramChecker()
        valid = False
        while not valid:
            valid = a.is_valid_word(input("Choose a word: "))
        a.get_anagrams()
        print(f"YOUR WORD: {a.word.upper()}")
        print("This is a valid English word.")
        print(f"{len(a.get_anagrams())} Anagrams for your word: {', '.join(a.get_anagrams()).lower()}.")


main()
