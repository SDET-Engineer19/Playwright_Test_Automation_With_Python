# mutability : It refers to the ability to change or edit the data in its memory location
#              It depends on the data type
# Immutable data types :  String, int, float, tuple,bool,complex
# Mutable data types : List, Set, Dictionary

# 1. Immutable Example for Strings :

val1 = "hello"
print(id(val1))
val1 = val1 + "world"
print(id(val1))  # new memory will be created, it will be changed

# 2. Immutable Example for tuples :

val2 = (900, 800, 700, 600, 500)
print(id(val2))  # new memory is created

val2 = val2 + (400, 300, 200, 100)
print(id(val2))  # another new memory allocation is created with new values


# 1. Mutable example:
l1 = [65, 66, 67]
print("Before Appending")
print(l1)
print(id(l1))

l2 = l1
l2.append(68)
print("After Appending")
print(l2)  # After Appending l2 and l1 will become same,
# since we have used aliasing and id of l2 & l1 are also same. Only possible for mutable data types
print(l1)
print(id(l2))

# Side effects of mutability
# If multiple developers are working in a project and if they are using any similar data type and out
# of which one developer has edited/changed the data type value, may be the change is not required for other developer.
# To avoid this, he/she can use cloning

l2 = l1[:]  # cloning :
# value of id changes for both the list
print(id(l2))
print(id(l1))


print("*******************************")

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print((id(t1)))
print(id(t2))
t3 = t2 + t1
print(t3)
print(id(t3))

# Practice Problems:
# 1. List of Tuples and then try to change the tuple values
t4 = (100, 200, 300, 400)
print(id(t4))
print(t4)


# t4[4] = 600
print(t4)   

## t4[4] = 600
print("After changing the tuple index value")
print(t4)
# 2. Tuple of List and then try to change the List values
# 3. Create two different list and append l2, l1, then verify the address
# 4. Create two different tuples and append l2, l1, then verify the address
