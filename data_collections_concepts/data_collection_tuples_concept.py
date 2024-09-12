from audioop import reverse

t1 = ()  # create empty tuple
print(t1)

t2 = (1, 2, 3, 4, 5)  # Homogenous
print(t2)

t3 = ("hello", 1, 7.8, True)
print(t3)  # Heterogeneous

# tuple with single data is not a tuple, it is either integer or string based on data type
T3 = ("Hello")
print(type(T3))

# by adding comma we can create single value tuple
T3 = ("Hello",)
print(T3)
print(type(T3))

# 2d tuples
t4 = (1, 2, 3, (4, 5))
print(t4)

# Tuples are immutable , cannot be changed once it is declared , whereas List is mutable
# So editing and adding the new value to tuple is not possible

# Delete :  can delete complete tuple , but we cannot delete specific value from tuple
# , but in list we can delete specific value in List

# del T3
# print(T3)

# Functions
print(len(t2))
print(max(t2))
print(min(t2))
print(sorted(t2))
print(sorted(t2, reverse=True))

for val in t2:
    print(val)
