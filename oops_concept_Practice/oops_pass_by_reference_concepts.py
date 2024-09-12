

class Customer:

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


def greet(customer):
    if customer.gender == "Male":
        print("Hello ", customer.name, "Sir")
    else:
        print("Hello ", customer.name, "ma'am")


cust = Customer("Kabira", "Male")
greet(cust)
cust1 = Customer("Geeta","Female")
greet(cust1)


# Static Variables
# Static Methods
# Inheritance Practice