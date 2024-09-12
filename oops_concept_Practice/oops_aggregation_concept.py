class Customer:

    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name,new_city, new_pincode, new_state):
        self.name = new_name
        self.address.change_address(new_city,new_pincode,new_state)
# if you want to change the name, pass the value while creating object
# if user don't want to change the name, pass it in edit_prfoile method as new_name=self.name

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_address(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state


add = Address("Hyderabad", 500019, "TG")
cust = Customer("Kabira", "Male", add)
cust.edit_profile("Tom","KPHB",182937,"AP")
print(cust)
print(cust.name)
print(cust.gender)
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
