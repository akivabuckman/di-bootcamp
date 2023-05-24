import menu_item
from menu_manager import MenuManager


def show_user_menu():
    choice = input("(V)iew item, (A)dd item, (D)elete item, (U)pdate item, (S)how menu, or (E)xit? ").upper()
    if choice == "V":
        print(MenuManager.all_items())
    elif choice == "A":
        name = input("Item name: ")
        price = int(input("Item price: "))
        menu_item.add_item_to_menu(name, price)
    elif choice == "D":
        name = input("Item name: ")
        price = int(input("Item price: "))
        menu_item.remove_item_from_menu(name, price)
    elif choice == "U":
        menu_item.update_item_from_menu()
    elif choice == "S":
        menu_item.show_restaurant_menu()
    elif choice == "E":
        menu_item.show_restaurant_menu()
    return choice


def main():
    while True:
        if show_user_menu() == "E":
            break


main()
