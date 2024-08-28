
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not found in your shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("Your shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = []
    while True:
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")
        choice = input("Choose an option(1-4): ")
        
        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif choice == "2":
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)
        elif choice == "3":
            view_list(shopping_list)
        elif choice == "4":
            print("Goodbye! Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
