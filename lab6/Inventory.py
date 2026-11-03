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
