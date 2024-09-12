# 1. Sets do not allow duplicate values
# 2. Sets have no Indexing and Slicing
# 3. Sets do not allow mutable data
# 4. Sets itself is a mutable data type


# Empty Set will be always Dict Type
S1 = {}
print(type(S1))

# To Create Empty Set, we need to create using below

s2 = set()
print(type(s2))

s3 = {1, 2, 3, 4, 5}
print(s3)
print(type(s3))

# verify duplicates allowing or not in set

s4 = {2, 8, 3, 7, 4, 9, 1, 6, 5, 10}
print(s4)

# Verify no indexing  should allow, should throw an error
# s4[4] = 500
# print(s4)
# Verify no slicing  should allow, should throw an error
# print(s4[0:3])

# Add value to set

s4.add(0)
print(s4)  # by default sort will be performed, if the set is unsorted

s5 = {3, 4, 1, 8, 11, 12}
# functions in sets
print(" ######### Set Functions ###########")

print("########### USE OF SET FUNCTIONS#########")
s6 = s4.union(s5)  # Returns the new set , which has  the common values from both sets
print(s6)
s7 = s4.intersection(s5)  # Returns the new set , only similar values from both sets
print(s7)

print(s7.pop())  # it should delete 4?, since set works on hashing, based on hashing the value is removed from set

print(len(s7))
print(s4)
print(s5)

print(s4.difference(s5))  # prints the uncommon data from the first set, common data from both set is not displayed

print(s5.difference(s4))  # prints the uncommon data from the first set, common data from both set is not displayed

print(s4.symmetric_difference(s5)) # prints the uncommon data from the both set

print(s4.issubset(s5))

print(s4.isdisjoint(s5))