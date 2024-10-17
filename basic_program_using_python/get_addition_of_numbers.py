val = "Kabira12345"
val = int(''.join((x for x in val if x.isnumeric())))
print(val)
b = 0
while val > 0:
    b += val % 10  # 12345 % 10 = 5
    val = val / 10  # 12345/10

print(b)
