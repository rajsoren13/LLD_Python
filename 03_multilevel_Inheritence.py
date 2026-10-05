class Device:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def info(self):
        return f"This is a brand {self.brand} available with a price at ${self.price}"

#intermediary Class inheritance
class SmartPhone(Device):
    def __init__(self, brand, price,camera):
        super().__init__(brand, price)
        self.camera=camera

    def details(self):
        return f"{self.brand} with a {self.camera} having price at ${self.price}"

#child class
class proSmartPhone(SmartPhone):
    def __init__(self, brand, price, camera,styles):
        super().__init__(brand, price, camera)
        self.styles=styles

    def prodetails(self):
        return f"{self.brand} is having a unique {self.styles} with a premium price ${self.price}"

#define class object
iphone=SmartPhone("Samsung",200,"Cannon")
cmr1=SmartPhone("iPhone",2300,"Fuzi")
prosmrt=proSmartPhone("ReadMe",40,"dezi","S-Pen")

result=iphone.info()
result1=cmr1.details()
result2=prosmrt.prodetails()
print(result)
print(result1)
print(result2)
