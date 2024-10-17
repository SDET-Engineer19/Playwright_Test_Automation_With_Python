a = 20
b = 10


def get_swap_numbers(value1, value2):
    print("Before Swapping : ", value1, value2)
    value1 = value1 + value2  # 10 + 20 = 30
    value2 = value1 - value2  # 30 - 10 = 20
    value1 = value1 - value2  # 30 - 20 = 10

    print("After Swapping : ",  value1, value2)


get_swap_numbers(a, b)

