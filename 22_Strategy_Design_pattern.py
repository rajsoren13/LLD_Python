class UPI:
    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI")


class CreditCard:
    def pay(self, amount):
        print(f"Paying ₹{amount} using Credit Card")


class PayPal:
    def pay(self, amount):
        print(f"Paying ₹{amount} using PayPal")


class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)

# Initially, select UPI
payment = PaymentService(UPI())
payment.make_payment(1000)

# Switch the strategy to Credit Card
payment.set_strategy(CreditCard())
payment.make_payment(2000)

card_payment = PaymentService(CreditCard())
card_payment.make_payment(2000)

paypal_payment = PaymentService(PayPal())
paypal_payment.make_payment(3000)