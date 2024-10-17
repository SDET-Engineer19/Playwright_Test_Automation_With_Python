def get_factorial_without_loop(val):
    if val == 0 or val == 1:
        return 1
    else:
        return val * get_factorial_without_loop(val - 1)


def get_factorial_with_loop(val):
    initial_val = 1
    for x in range(1, val+1):
        initial_val *= x
    print(initial_val)


class Factorial_Logic:
    factorial_num = get_factorial_without_loop(5)
    print(factorial_num)
    get_factorial_with_loop(5)
