# for val in range(1, 20, 2):
#     print(val)

list_numbers = list(range(10, 20))
# print(list_numbers)

for x in list_numbers:
    for y in range(1, x):
        print(y, end=' ')
    print(" ")

