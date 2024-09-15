# type conversion :  when user enter passes any input value to input() prompt , by default it will be in string data
# type
#  We have two types of type conversion : 1. Implicit 2. Explicit
# Implicit
print(10 + 12)
print(4.5 + 9)
print((5.9 + 8.9))
print(22.7 - 13.8)

# Explicit can be performed using predefined functions

first_num = int(input("Enter First Number : "))
second_num = int(input("Enter Second Number : "))

print(first_num)
print(second_num)

result = first_num + second_num
print(result)

a = float(input("Enter Double Digit Value : "))
b = float(input("Enter Double Digit Value : "))

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
