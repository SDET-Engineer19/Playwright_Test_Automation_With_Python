# default argument function

def is_even(number):
    if type(number) == int:
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    else:
        print("Not Allowed")


print(is_even("3"))
