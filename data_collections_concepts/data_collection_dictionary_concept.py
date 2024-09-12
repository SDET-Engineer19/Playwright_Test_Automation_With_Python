# 1. No Indexing
# 2. Dictionary is Mutable type
# 3. Keys are immutable and values are mutable
# 4. Keys should be unique

# Mutable : List/Set/Dictionary
# Immutable: tuples/int/Strings/float/Boolean/Complex

# 1.  Create
# 2.  Access
# 3.  Edit
# 4.  Delete
# 5. Functions

user_details = {"name": "Kabira", "role": "SDET"}
print(user_details)

# d1 = {[1,2,3]:"kabira"}
# print(d1) # it is mutable type

d2 = {"Name": "Tom", "role": "Dev"}
print(d2)

# indexing doesn't work , we can use keys to get value from dict

print(d2["Name"])
print(d2["role"])

# we can edit the using key and value should new data
d2["Name"] = "Peter"
print(d2)

# Adding new keys to the existing dict

d2["Age"] = 23
print(d2)

# Creating 2D dictionary

d3 = {
    "Name": "Sunil",
    "College": "JNTUH",
    "std_id": 2939,
    "Marks":
        {
            "M1": 98,
            "DSA": 78,
            "CKA": 62
        }
}

print(d3)
# Get the value of DSA from 2D Dict
print(d3['Marks']["DSA"])

# Delete Dict

d4 = {"Name": "Tom", "role": "Dev"}
del d4
# print(d4)
# Empty Dict
d4 = {"Name": "Tom", "role": "Dev"}
d4.clear()  # Empty Dict
print(d4)

# Printing keys in dict using loops

for key in d3:
    print(key)

# Printing key and values in dict using loops
for key in d3:
    print(key,d3[key])

    # Printing only values in dict using loops
for key in d3:
    print(d3[key])