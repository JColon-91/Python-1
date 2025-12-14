'''
You are tasked with creating a simple inventory management system for a market. The system should allow users to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.
Functionality:
    Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.
    Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.
    View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
    Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.
    Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.
Project Structure:
    Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.
    Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the inventory.
    Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding, updating, viewing, removing items, or searching by category.
'''

# Inventory List:
inventory = []

# Functions:
def add_item():
    try:
        name = input("Enter item name: ").strip()
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        category = input("Enter item category: ").strip()

        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        }

        inventory.append(item)
        print(f"Item '{name}' added successfully!\n")

    except ValueError:
        print("Error: Price must be a number and quantity must be an integer.\n")

def update_item():
    name = input("Enter the name of the item to update: ").strip()
    found = False
    for item in inventory:
        if item["name"].lower() == name.lower():
            found = True
            try:
                new_price = float(input("Enter new price: "))
                new_quantity = int(input("Enter new quantity: "))
                new_category = input("Enter new category: ").strip()

                item["price"] = new_price
                item["quantity"] = new_quantity
                item["category"] = new_category

                print(f"Item '{name}' updated successfully!\n")
            except ValueError:
                print("Error: Price must be a number and quantity must be an integer.\n")
            break
    if not found:
        print(f"Item '{name}' not found in inventory.\n")

def view_inventory():
    if not inventory:
        print("Inventory is empty.\n")
        return
    print("\n*** Current Inventory ***")
    for idx, item in enumerate(inventory, start=1):
        print(f"{idx}. Name: {item['name']}, Price: {item['price']}, "
              f"Quantity: {item['quantity']}, Category: {item['category']}")
    print("")

def remove_item():
    name = input("Enter the name of the item to remove: ").strip()
    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)
            print(f"Item '{name}' removed successfully!\n")
            return
    print(f"Item '{name}' not found in inventory.\n")

def search_by_category():
    category = input("Enter the category to search: ").strip()
    found_items = [item for item in inventory if item["category"].lower() == category.lower()]
    if found_items:
        print(f"\nItems in category '{category}':")
        for item in found_items:
            print(f"- Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
        print("")
    else:
        print(f"No items found in category '{category}'.\n")

#Main Menu Loop
def main():
    while True:
        print("***** MARKET INVENTORY SYSTEM *****")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")
        print("**********************************")

        option = input("Choose an option from 1 to 6: ").strip()

        if option == "1":
            add_item()
        elif option == "2":
            update_item()
        elif option == "3":
            view_inventory()
        elif option == "4":
            remove_item()
        elif option == "5":
            search_by_category()
        elif option == "6":
            print("Exiting program: Goodbye!")
            break
        else:
            print("Invalid choice, try again!\n")

#Run the Inventory System

if __name__ == "__main__":
    main()