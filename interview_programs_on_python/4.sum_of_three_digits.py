def get_sum_of_three_digits(l1=list()):
    temp = 0
    if len(l1) > 1:
        for val in l1:
            temp += val
        return temp
    else:
        return temp


class sum_of_three_digits:
    l1 = get_sum_of_three_digits([10, 20, 30])
    print("Sum of list : ", l1)
