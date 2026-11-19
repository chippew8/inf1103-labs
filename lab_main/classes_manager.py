import json
import csv
from pathlib import Path
from Inventory import Inventory
from Product import DigitalProduct, PhysicalProduct, ProductFactory
from Supplier import Supplier
from Order import Order
from OrderLine import OrderLine

def display_all(inventory):
    inventory.display_all()

def add_product(inventory):
    print("Add New Product")
    product_type = input("Select product type (Digital/Physical): ")
    id = input("Product ID: ")
    name = input("Product Name: ")
    price = get_positive_float("Price: ")
    quantity = get_positive_float("Stock Quantity: ")
    print(price)
    product = ProductFactory.create(product_type, id, name, price, quantity, new_supplier)
    print(type(product))
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
                            product = PhysicalProduct(id, values["Name"], values["Price"], values["Stock"], None, values["Weight"])
                        if values["Type"] == "Digital":
                            product = DigitalProduct(id, values["Name"], values["Price"], values["Stock"], None, values["Download Size"])
                        inventory.add_product(product)
                return inventory 
            except:
                return inventory
    else:
        new_file = open('inventory.json', 'w+')
        new_file.close()
        return inventory

def load_products(path:str, inventory: Inventory, supplier: Supplier):
    try:
        file = open(path, newline="")
    except FileNotFoundError:
        print(f"Product file is not found: {path}")
    else:
        with file:
            next(file, None)
            next(file, None)
            for row in file:
                try:
                    list = row.split(",")
                    inventory.add_product(ProductFactory.create(list[0], list[1], list[2], list[3], list[4], supplier))

                    next(file, None)
                except ValueError:
                    print(f"{list[2]} failed to load")
                    next(file, None)
                    continue
        print(f"{len(inventory.get_product_list())} products loaded")
    finally:
        print("Load attempt finished")
                

def get_positive_float(prompt:str) -> float:
    while True:
        try: 
            value = float(input(prompt))
            if value <= 0 :
                print("Please enter a number greater than a zero")
                continue
            return value
        except ValueError:
            print("Please enter a valid number, e.g. 12.50")





print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================\n")
inventory = Inventory()
new_supplier = Supplier("S0001", "Supplier 1", "first.supplies@gmail.com")
load_products("products.csv", inventory, new_supplier)
# load_inventory(inventory)

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