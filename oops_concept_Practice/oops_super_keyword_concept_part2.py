class Phone:

    def __init__(self, price, brand, camera):
        print("Inside Phone Constructor")
        self.price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        print("Inside SmartPhone Constructor")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram


s = SmartPhone(20000, "Apple", 20,"MacOs",32)
print(s.os)
print(s.brand)
