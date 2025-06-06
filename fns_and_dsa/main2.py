
from shopping_list_manager import display_menu, add_item, remove_item, view_list

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()