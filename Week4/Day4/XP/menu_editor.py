import menu_item
from menu_manager import MenuManager
def show_user_menu():
    choice = input("(V)iew item, (A)dd item, (D)elete item, (U)pdate item, or (S)how menu?").upper()
    if choice == "V":
        MenuManager.all_items()
    elif choice == "A":
        name = input("Item name: ")
        price = int(input("Item price: "))
        menu_item.add_item_to_menu(name, price)

# it doesn't make sense that the delete function should not interact with the menu itself. how can it create an object
# that is deleted?