from Product import Product

class Inventory:
    def __init__(self):
        self.__product_list: list[Product] = []

    def add_product(self, product:Product) -> None:
        self.__product_list.append(product)

    def delete_product(self, id:str) -> None:
        self.__product_list.remove(self.search_product(id))

    def search_product(self, id:str) -> Product | None:
        for things in self.__product_list:
            if things.get_id() == id:
                return things
        print("Item not found")
        return

    def display_all(self) -> None:
        print("\n")
        print("--------------------------------")
        print("Current Inventory")
        for product in self.__product_list:
            product.display_information()
            print(product.get_fulfilment_info())
        print("--------------------------------")

    def get_product_list(self) -> list:
        return self.__product_list
