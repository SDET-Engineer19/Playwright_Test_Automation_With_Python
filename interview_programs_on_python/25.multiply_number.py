def get_multiplication_value(value1, value2):

    total = 0
    if value1 == 0 and value2 == 0:
        return 0
    elif value1 < 0 and value2 < 0:
        value1 = abs(value1)
        value2 = abs(value2)

    for val in range(0, value2): # 0 , 8 6
        total += value1

    return total


class Calculate_Two_Multiplication:
    val1 = int(input("Enter Value1 : "))
    val2 = int(input("Enter Value2 : "))

    val = get_multiplication_value(val1, val2)
    print(val)
