class coffeeOrder:
    def __init__(self,customer_name,drink_type,size):
        self.customer_name=customer_name               #public attribute
        self.drink_type=drink_type                     #public attribute
        self.size=size                                 #public attribute
        self.__price=5.0                                   #private attribute(hidden)
    #public method
    def get_order_summary(self):
        return f"{self.customer_name} ordered a {self.size} {self.drink_type}"
    #private method
    def __calculate_price(self):
        return f"total price:$ {self.__price}"
    #public metgod
    def get_price(self):
        return self.__calculate_price()


order=coffeeOrder("Raj","Latte","Large")
#Access public attributre
print(order.customer_name)
print(order.get_order_summary())
print(order.get_price())

#Access private attribute:if run will display error for it
#print(order.__price)
#print(order.__calculate_price())