import json
from pathlib import Path

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print("--------------------------------")
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price}")
        print(f"Stock: {self.__stock}\n")
        print("--------------------------------")

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

class Inventory:
    def __init__(self):
        self.__product_list = []

    def add_product(self, product):
        self.__product_list.append(product)

    def search_product(self, product):
        for things in self.__product_list:
            if things.get_id() == product:
                return things
        print("Item not found")
        return

    def display_all(self):
        print("\n")
        print("--------------------------------")
        print("Current Inventory")
        for product in self.__product_list:
            product.display_information()
        print("--------------------------------")

    def get_product_list(self):
        return self.__product_list



def display_all(inventory):
    inventory.display_all()

def add_product(inventory):
    print("Add New Product")
    id = input("Product ID: ")
    name = input("Product Name: ")
    price = input("Price: ")
    quantity = input("Stock Quantity: ")
    product = Product(id, name, price, quantity)
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
        dictionary[entry.get_id()] = {
            "Name": entry.get_name(),
            "Price": entry.get_price(),
            "Stock": entry.get_stock()
        }
    print("Saving inventory before exit...")
    with open('inventory.json', 'w+') as json_file:
        json.dump(dictionary, json_file)
    print("Inventory saved successfully.")

def load_inventory(inventory):
    if Path('inventory.json').is_file():
        with open('inventory.json','r') as json_file:
            json_data = json.load(json_file)
            print("inventory.json found.")
            print("Inventory loaded successfully.")
            for id in json_data:
                if id is not None:
                    values = json_data.get(id)
                    name = values["Name"]             
                    price = values["Price"]
                    stock = values["Stock"]
                    product = Product(id, name, price, stock)
                    inventory.add_product(product)
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