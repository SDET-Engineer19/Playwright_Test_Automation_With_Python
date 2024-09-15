print(list(range(1, 11)))  # range is a function where it start the value from and stops the value-1 i.e 10

print(tuple(range(0, 5)))  # starts from 0 and ends at 4

print(list(range(6)))  # By default starts at 0, if there is no start value and ends at end - 1

print(list(range(10, 0, -1)))  # Reverse the number by using negative numbers

print((tuple(range(5, 1, -1))))  # 5,4,3,2

print(list(range(1, 11,3)))  # we can skip the values by passing third variable in range function, o/p: 1,4,7,
                                           # 10 ( will skip for every 2 values)

for val in range(10, 20):
    print(val)

print("################")

for val in range(1,10,2):
    print(val)

# Nested Loops:

# print sequence using nested loops

# *
# **
# ***
# ****
# *****
print("################")

for row in range(1,5):
    for col in range(0,row):
        print("*",end=" ")
    print(" ")