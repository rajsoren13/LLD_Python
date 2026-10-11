
class UPI:
    def pay(self):
        print("Payment through UPI")


class Card:
    def pay(self):
        print("Payment through CARD")


class NetBanking:
    def pay(self):
        print("Payment through NET BANKING")


class Wallet:
    def pay(self):
        print("Payment through Wallet")


payment_method = UPI()
payment_method.pay()

