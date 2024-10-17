def validate_number_is_divisible(num):
    if num % 3 == 0 and num % 6 == 0:
        print(num, "is divisible by 3 & 6 ")
    else:
        print(num, "is not divisible by 3 & 6 ")


class verify_any_number_is_divisible_or_not:
    num = int(input("Enter Number : "))
    validate_number_is_divisible(num)
