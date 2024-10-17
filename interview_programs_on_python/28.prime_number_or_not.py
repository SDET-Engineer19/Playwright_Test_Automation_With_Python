def verify_entered_number_is_prime(num):
    flag = False
    if num > 1:
        for val in range(2, (num // 2) + 1):
            if num % val == 0:
                print(num, "is not a prime number")
                flag = True
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
    return flag


class Verify_Prime_Number:
    num = int(input("Enter Number : "))
    verify_entered_number_is_prime(num)
