def count_num_of_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_num_of_digits(num // 10)


def check_armstrong_number_or_not(armstrong_num):
    b = count_num_of_digits(armstrong_num)
    temp_val = 0
    while armstrong_num != 0:
        a = armstrong_num % 10
        temp_val += pow(a, b)
        armstrong_num //= 10

    return temp_val


class ArmStrong_Number:
    num = int(input("Enter Number : "))
    temp_val = check_armstrong_number_or_not(num)
    if temp_val == num:
        print("Resulted Num : {0} and it is a ArmStrong Number".format(temp_val))
    else:
        print("Resulted Num : {0} and it is not a ArmStrong Number".format(temp_val))
