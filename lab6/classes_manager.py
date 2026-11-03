import json
from pathlib import Path
from Inventory import Inventory
from Product import DigitalProduct, PhysicalProduct

def display_all(inventory):
    inventory.display_all()

def add_product(inventory):
    print("Add New Product")
    product_type = input("Select product type (Digital/Physical): ")
    if product_type == "Physical":
        id = input("Product ID: ")
        name = input("Product Name: ")
        price = input("Price: ")
        quantity = input("Stock Quantity: ")
        weight = input("Weight: ")
        product = PhysicalProduct(id, name, price, quantity, weight)
    elif product_type == "Digital":
        id = input("Product ID: ")
        name = input("Product Name: ")
        price = input("Price: ")
        quantity = input("Stock Quantity: ")
        download_size = input("Download Size: ")
        product = DigitalProduct(id, name, price, quantity, download_size)
    else:
        print("Unknown product type. Try Again.")
    inventory.add_product(product)
    print("Product added successfully!")
    return inventory

def update_stock(inventory):
    print("Update Stock")
    id = input("Enter Product ID: ")
    product = inventory.search_product(id)
    if product is not None:
        print("Product Found:")
        print(f"Name: {product.get_name()}")
        print(f"Stock: {product.get_stock()}\n")

        new_stock = input("New Stock Quantity:")
        product.update_stock(new_stock)
        print("Stock updated successfully!")
    else:
        print("No existing product found")
    
def search_product(inventory):
    print("Search Product")
    id = input("Enter Product ID: ")
    product = inventory.search_product(id)
    if product is not None:
        print("\n")
        print("--------------------------------")
        print("Product Found!")
        product.display_information()
        print("--------------------------------")

    else:
        print("No existing product found.")
        return
     
def save_inventory(inventory):
    dictionary = {}
    for entry in inventory.get_product_list():
        if isinstance(entry, PhysicalProduct):
            dictionary[entry.get_id()] = {
                "Type": "Physical",
                "Name": entry.get_name(),
                "Price": entry.get_price(),
                "Stock": entry.get_stock(),
                "Weight": entry.get_weight(),
                "Download Size": None
            }
        elif isinstance(entry, DigitalProduct):
            dictionary[entry.get_id()] = {
                "Type": "Digital",
                "Name": entry.get_name(),
                "Price": entry.get_price(),
                "Stock": entry.get_stock(),
                "Weight": None,
                "Download Size": entry.get_download_size()
            }
    print("Saving inventory before exit...")
    with open('inventory.json', 'w+') as json_file:
        json.dump(dictionary, json_file)
    print("Inventory saved successfully.")

def load_inventory(inventory):
    if Path('inventory.json').is_file():
        with open('inventory.json','r') as json_file:
            try:
                json_data = json.load(json_file)
                print("inventory.json found.")
                print("Inventory loaded successfully.")
                for id in json_data:
                    if id is not None:
                        values = json_data.get(id)
                        if values["Type"] == "Physical":
                            product = PhysicalProduct(id, values["Name"], values["Price"], values["Stock"], values["Weight"])
                        if values["Type"] == "Digital":
                            product = DigitalProduct(id, values["Name"], values["Price"], values["Stock"], values["Download Size"])
                        inventory.add_product(product)
                return inventory 
            except:
                return inventory
    else:
        new_file = open('inventory.json', 'w+')
        new_file.close()
        return inventory
        

print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")
inventory = Inventory()
load_inventory(inventory)
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
            dictionary = display_all(inventory)
        case 2:
            dictionary = add_product(inventory)
        case 3:
            dictionary = update_stock(inventory)
        case 4:
            dictionary = search_product(inventory)
        case 5:
            dictionary = save_inventory(inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated")
            break
        case 6:
            break
        case _:
            print("Not a valid option.")