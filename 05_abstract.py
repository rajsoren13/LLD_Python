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
    #private method to brew coffee
    def __brew(self):
        #step involve in brewing the coffee
        return f"Brewing a {self.size} for {self.customer_name}"

    #public method
    def make_coffee(self):
        print(f"Placed order by {self.customer_name}")
        return self.__brew()


order=coffeeOrder("Soren","Cappuccino","Medium")

#using abastraction make coffee
print(order.make_coffee())
