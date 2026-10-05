class Device:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def info(self):
        return f"This is a brand {self.brand} available with a price at ${self.price}"

#Child Class inheritance
class SmartPhone(Device):
    def __init__(self, brand, price,camera):
        super().__init__(brand, price)
        self.camera=camera

    def details(self):
        return f"{self.brand} with a {self.camera} having price at ${self.price}"


iphone=SmartPhone("Samsung",200,"Cannon")
cmr1=SmartPhone("iPhone",2300,"Fuzi")

result=iphone.info()
result1=cmr1.details()
print(result)
print(result1)
