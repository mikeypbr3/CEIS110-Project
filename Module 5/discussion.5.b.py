# AI Version with a little fine tuining.
import os

# Initialize an empty shopping list
shopping_list = []

def add_item():
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

def view_list():
    """Display the current shopping list."""
    if shopping_list:
        print("Current shopping list:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
    else:
        print("The shopping list is empty.")

def save_list():
    """Save the current shopping list to a file."""
    filename = input("Enter filename to save the list: ")
    with open(filename, 'w') as file:
        for item in shopping_list:
            file.write(item + '\n')
    print(f"List saved to {filename}")

def load_list():
    """Load a shopping list from a file."""
    filename = input("Enter filename to load the list from: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            global shopping_list
            shopping_list = [line.strip() for line in file]
        print(f"List loaded from {filename}")
    else:
        print("File not found.")

def view_saved_lists():
    """View all saved shopping list files."""
    files = [f for f in os.listdir() if f.endswith('.txt')]
    if files:
        print("Saved shopping lists:")
        for file in files:
            print(file)
    else:
        print("No saved shopping lists found.")

def main():
    """Main program loop."""
    while True:
        print("\nShopping List Menu:")
        print("1. Add item")
        print("2. View current list")
        print("3. Save list")
        print("4. Load list")
        print("5. View saved lists")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_list()
        elif choice == '3':
            save_list()
        elif choice == '4':
            load_list()
        elif choice == '5':
            view_saved_lists()
        elif choice == '6':
            print("Thank you for using the Shopping List Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    print("This program was generated by Claude, an AI assistant created by Anthropic.")