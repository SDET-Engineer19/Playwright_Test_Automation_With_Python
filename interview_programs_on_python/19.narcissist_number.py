def count_num_of_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_num_of_digits(num // 10)


def verify_narcissist_number_or_not(num):
    count = count_num_of_digits(num)
    temp_val = 0
    new_val = num
    while new_val:
        temp_val += pow(new_val % 10, count)
        new_val = new_val // 10
    return temp_val


class Narcissist_Number:

    num = int(input("Enter Any Number : "))
    narcissist_num = verify_narcissist_number_or_not(num)
    if narcissist_num == num:
        print("Entered Number {0} and it is a Narcissist Number ".format(narcissist_num))
    else:
        print("Entered Number {0} and it is not a Narcissist Number ".format(narcissist_num))


