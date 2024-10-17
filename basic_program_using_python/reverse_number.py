num = int(input("Enter Number : "))
temp = 0
while num != 0:
    a = num % 10
    temp = temp * 10 + a
    num //= 10

if temp != num:
    print("Number is Reversed : ", temp)
else:
    print("Number is Not Reversed")
