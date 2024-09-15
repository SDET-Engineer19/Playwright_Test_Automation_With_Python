c = "Hello" + "-" + "World"  # Arthemtic Operators
print(c)

print("*" * 50)  # Relational Operators ( > * < )
print("Hello" * 4)  # Relational Operators (*)

if "Mumbai" > "Pune":
    print("Valid")
else:
    print("Invalid")

if "Hyderabad" > "Lingampally":
    print("True")
else:
    print("False")

# Operators on data_type_strings_concepts
print("" or "world")  # 0 or 1 :  1
print("hello" or "")  # 1 or 0:  1
print("hello" or "world")  # 1 or 1 :  1
print("" or "")  # 0 or 0 : 0(nothing) 0

print("hello" and "")  # 1 and 0 : 0
print("" and "world")  # 0 and 1 : 0
print("hello" and "world")  # 1 and 1 : 1
print("" and "")  # 0 and 0 : 0

# Non-Empty data_type_strings_concepts are False
print(not "hello")
print(not "False")
print(not "True")  # False
# Empty data_type_strings_concepts are True
print(not "")  # True
