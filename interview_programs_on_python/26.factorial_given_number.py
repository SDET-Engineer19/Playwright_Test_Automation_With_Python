def get_factorial_of_number(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * get_factorial_of_number(num - 1)


class Factorial_Number:
    value = int(input("Enter Any Number : "))
    factorial_num = get_factorial_of_number(value)
    print("Factorial Number of {0} is ".format(value), factorial_num)
