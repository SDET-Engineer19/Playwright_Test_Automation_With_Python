def get_square_of_each_digit(a, b, c):
    total_val = (a * a) + (b * b) + (c * c)
    return total_val


class Square_Digit_Number:

    a = int(input("Enter ""a"" value : "))
    b = int(input("Enter ""b"" value : "))
    c = int(input("Enter ""c"" value : "))

    total_val = get_square_of_each_digit(a, b, c)
    print("Sum of Square all three numbers : ", total_val)
