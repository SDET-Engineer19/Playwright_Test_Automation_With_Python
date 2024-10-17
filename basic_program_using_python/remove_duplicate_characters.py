user_name = "Kabira"

user_name_set = set()
# using set
for val in user_name:
    user_name_set.add(val)

print(user_name_set)

# without set

p = " "

for char in user_name:
    if char not in p:
        p += char
print(p)

