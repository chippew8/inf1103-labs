from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total:float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total:float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def apply(self, total:float, percentage: int) -> float:
        return total*(100-percentage)/100

class BulkDiscount(DiscountStrategy):
    def apply(self, total: float, threshold: int, percentage: int) -> float:
        return total*(100-percentage)/100 if total > threshold else total

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float):
        return total * 0.95