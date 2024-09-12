class Phone:

    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")


class SmartPhone(Phone):

    def buy(self):
        print("Buying a SmartPhone")
        super().buy() # calling all parent onstructor and methods : super
                              # Super keyword always inside method, not outside class


s = SmartPhone(20000,"Apple",20)
s.buy()
