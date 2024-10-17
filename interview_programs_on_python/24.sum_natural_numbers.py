def get_sum_of_natural_numbers(num):
    natural_num_list = list(range(0, num+1))
    total_sum_val = 0
    for val in natural_num_list:
        total_sum_val += natural_num_list[val-1]
    return total_sum_val


class Calculate_Sum_NaturalNumbers:
    num = int(input("Enter Number : "))
    total_sum_val = get_sum_of_natural_numbers(num)
    print("Sum for first ", num, " natural number is {0}".format(total_sum_val))
