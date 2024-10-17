def get_odd_numbers(num):
    odd_number_list = list(range(1, num+1, 2))
    print(odd_number_list)
    print(len(odd_number_list))


class First_Twenty_Five_Odd_Numbers:

    num = int(input("Enter Number to Display first twenty Odd Numbers : "))
    get_odd_numbers(num)