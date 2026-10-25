class ThirdPartyPayment:
    def make_payment(self, amount):
        print(f"Processing payment of ₹{amount}")

class PaymentAdapter:
    def __init__(self,third_party_payment):
        self.third_party_payment=third_party_payment
    def pay(self,amount):
            self.third_party_payment.make_payment(amount)
        
class PaymentService:
    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)

# Create the third-party payment object
third_party = ThirdPartyPayment()

# Wrap it with the adapter
adapter = PaymentAdapter(third_party)

# Pass the adapter to our application
payment = PaymentService()
payment.process_payment(adapter, 1000)