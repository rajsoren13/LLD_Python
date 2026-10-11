from abc import ABC,abstractmethod

#correct way satisfying SOLID PRICIPLE-O
  # this acts as the interface
class Discount(ABC):
    @abstractmethod
    def apply(self,price):
        pass

class RegularDiscount(Discount):
    def apply(self, price):
        return price * 0.95

class PremiumDiscount(Discount):
    def apply(self, price):
        return price * 0.90

class VIPDiscount(Discount):
    def apply(self, price):
        return price * 0.80
#Write the calculator so it only depends on the abstraction.
class DiscountCalculator:
    # discount: Discount points to the Discount(ABC) class.
    # And if you write only discount, nothing changes when the code runs.
    #Both versions work identically, because Python ignores type hints at runtime.
    def calculate(self, discount: Discount, price):
        return discount.apply(price)

calc = DiscountCalculator()

print(calc.calculate(RegularDiscount(), 1000))   # 950.0
print(calc.calculate(PremiumDiscount(), 1000))   # 900.0
print(calc.calculate(VIPDiscount(), 1000))       # 800.0