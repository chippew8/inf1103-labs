from OrderLine import OrderLine
from Product import Product
class Order():
    def __init__(self, order_id: str):
        self.__order_id = order_id
        self.__order_lines: list[OrderLine]= []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0
        for order_line in self.__order_lines:
            print(f"The cost of {order_line.get_product().get_name()} is {order_line.get_product().get_price()}")
            total += order_line.calculate_subtotal()
        return total

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list:
        return self.__order_lines

    def remove_order_line(self, product_id:str) -> None:
        for order_line in self.__order_lines:
            if order_line.get_product().get_id() == product_id:
                print(f"{order_line.get_product().get_name()} has been removed")
                self.__order_lines.remove(order_line)
                return