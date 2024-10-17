list_numbers = [100, 200, 300, 400, 500]

max_val = list_numbers[0]
min_val = list_numbers[0]

list_len = len(list_numbers)
for val in list_numbers:
    if val > max_val:
        max_val = val
    elif val < min_val:
        mi_val = val

print(max_val)
print(min_val)
