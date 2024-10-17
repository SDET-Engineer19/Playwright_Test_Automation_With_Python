def get_reverse_any_number(num):
    flag = False
    is_reverse = 0
    while num != 0:
        a = num % 10
        is_reverse = is_reverse * 10 + a
        num //= 10

    if is_reverse != num:
        flag = True
        print("Number is Reversed to : ", is_reverse)
    else:
        flag = False
        print("Number is Not Reversed to : ", is_reverse)

    return flag


class reverse_entered_number:
    num = int(input("Enter Natural Number : "))
    flag = get_reverse_any_number(num)
    if flag:
        print("Entered Number is Reversed  ")
    else:
        print("Entered Number is Not Revered ")
