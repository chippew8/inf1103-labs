from OrderLine import OrderLine
from Product import Product
from DiscountStrategy import DiscountStrategy, NoDiscount

class Order():
    def __init__(self, order_id: str, discount: DiscountStrategy = NoDiscount()):
        self.__order_id = order_id
        self.__order_lines: list[OrderLine]= []
        self.__discount: DiscountStrategy = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)

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

    def set_discount(self, discount: DiscountStrategy):
        self.__discount: DiscountStrategy = discount