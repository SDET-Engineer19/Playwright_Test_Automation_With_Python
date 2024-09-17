# Keyword Function

def flexi(*number):
    product = 1
    print(number)
    print(type(number))
    for i in number:
        product = product * i
    print(product)


flexi(1, 2, 3)  # python interpreter will convert the numbers into tuples
flexi(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
