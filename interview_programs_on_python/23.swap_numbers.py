def get_swap_numbers(value1, value2):
    print("Before Swapping : ", value1, value2)
    value1 = value1 + value2  # 10 + 20 = 30
    value2 = value1 - value2  # 30 - 10 = 20
    value1 = value1 - value2  # 30 - 20 = 10

    print("After Swapping : ",  value1, value2)


class Swapping_Numbers:

    a = int(input("Enter ""a"" value : "))
    b = int(input("Enter ""b"" value : "))

    get_swap_numbers(a, b)
