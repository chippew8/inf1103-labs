import json
from pathlib import Path

def display_all(dictionary):
    print("Current Inventory")
    print("-------------------------")
    for entry in dictionary.keys():
        print(f"ID: {entry} | Name: {dictionary[entry]['Name']} | Price: ${dictionary[entry]['Price']} | Stock: {dictionary[entry]['Stock']} ")
    print("-------------------------")
    return dictionary

def add_product(dictionary):
    print("Add New Product")
    id = input("Product ID: ")
    name = input("Product Name: ")
    price = input("Price: ")
    quantity = input("Stock Quantity: ")
    dictionary[id]= {
        "Name" : name,
        "Price" : price,
        "Stock" : quantity
    }
    print("Product added successfully!")
    return dictionary

def update_stock(dictionary):
    print("Update Stock")
    id = input("Enter Product ID")
    if dictionary[id] is not None:
        print("Product Found:")
        print(f"Name: {dictionary[id]['Name']}")
        print(f"Stock: {dictionary[id]['Stock']}\n")

        new_stock = input("New Stock Quantity:")
        dictionary[id]["Stock"] = new_stock
        print("Stock updated successfully!")
    return dictionary

def search_product(dictionary):
    print("Search Product")
    id = input("Enter Product ID")
    if dictionary[id] is not None:
        print("Product Found:")
        print("--------------------------------")
        print(f"ID: {id}")
        print(f"Name: {dictionary[id]['Name']}")
        print(f"Price: ${dictionary[id]['Price']}")
        print(f"Stock: {dictionary[id]['Stock']}\n")
        print("--------------------------------")
    return dictionary
    
     
def save_inventory(dictionary):
    print("Saving inventory before exit...")
    with open('inventory.json', 'w+') as json_file:
        json.dump(dictionary, json_file)
    print("Inventory saved successfully.")


def load_inventory():
    if Path('inventory.json').is_file():
        with open('inventory.json','r') as json_file:
            json_data = json.load(json_file)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            return json_data 
    else:
        new_file = open('inventory.json', 'w+')
        new_file.close()
        return {}
        

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")
dictionary = load_inventory()
while True:
    print("\n-------MENU-------")
    print("1. Display All Products")
    print("2. Add Products")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-------------------\n")

    menu_choice = input("Enter option: ")
    match int(menu_choice):
        case 1:
            dictionary = display_all(dictionary)
        case 2:
            dictionary = add_product(dictionary)
        case 3:
            dictionary = update_stock(dictionary)
        case 4:
            dictionary = search_product(dictionary)
        case 5:
            dictionary = save_inventory(dictionary)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated")
            break
        case 6:
            break
        case _:
            print("Not a valid option.")