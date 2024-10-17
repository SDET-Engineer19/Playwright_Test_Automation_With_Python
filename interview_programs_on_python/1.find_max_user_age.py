def get_max_user_age():
    max_age = 0
    a = int(input("Enter User ""a"" age : "))
    b = int(input("Enter User ""b"" age : "))
    c = int(input("Enter User ""c"" age : "))
    if a > b:
        max_age = a
    elif b > c:
        max_age = b
    elif c > a:
        max_age = c
    print("The maximum age of a person is ", max_age)



class max_user_age:
    get_max_user_age()

