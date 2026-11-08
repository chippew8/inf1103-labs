from abc import ABC, abstractmethod
import CanBeShipped
from Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier = supplier

    def update_stock(self, quantity:int) -> None:
        self.__stock = quantity
        
    def display_information(self) -> None:
        print("\n--------------------------------")
        print(f"ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price}")
        print(f"Stock: {self.__stock}")

    def get_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock

    def get_supplier(self) -> Supplier:
        return self.__supplier
    
    @abstractmethod
    def get_fulfilment_info(self):
        pass

class PhysicalProduct(Product, CanBeShipped.CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.__weight}Kgs")

    def get_fulfilment_info(self) -> str:
        return f"{self.get_name()} requires physical shipping"

    def calculate_shipping_cost(self) -> str:
        return f"It cost ${int(self.get_weight())*2} to ship {self.get_name()}"

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: int):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    def get_download_size(self) -> float:
        return self.__download_size

    def display_information(self) -> str:
        super().display_information()
        print(f"Download Size: {self.__download_size}MBs")

    def get_fulfilment_info(self) -> str:
        return f"{self.get_name()} is digital"


