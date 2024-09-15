for i in range(1,11):
    if i == 9:
        break
    print(i,end = " ")
print(" ")

# Program to display odd numbers which are not divisble by 3
for val in range(1,20,2):
    if val%3 == 0:
        continue
    print(val,end = " ")
print(" ")

print("##############################")

# we use pass keyword, if the method or loop implementation is yet to be developed
for col in range(1,10):
    pass