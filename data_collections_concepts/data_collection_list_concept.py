# Homogenous List
from audioop import reverse

from arrays_development_Practice.basic_concept_of_ArrayMethods import numbers

number_List = [1, 2, 3, 4, 5]
print(number_List)

print(number_List[-1])  # displays last digit
print(number_List[::-1])  # reversing the list

# Hetrogenous List
num_hetro_List = [20, "Car", 'A', True, (4 + 2j), 2.3]
print(num_hetro_List)

# Multi Dimensional Array 2D

L2 = [1, 2, 3, [4, 5]]
print(L2)
print(L2[0])
print(L2[-1][0])  # 2nd List first Value
print(L2[-1])  # Alternative way of getting 2nd List Array

# 3 Dimensional Array

L3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(L3)

print(L3[0][1][0])  # prints 1st List 1st Value
print(L3[0][1][1])  # prints 1st List 1st Value
# Alternative way using negative indexing

print(L3[0][-1][-2])
print(L3[1][-1][-2])

# Editing the list , as List are Mutable in Python

number_List[0] = 200  # can change the value of specific index
print(number_List)

# using silicing we can change multiple values

number_List[0:5] = [100, 200, 300, 400, 500]
print(number_List)

# append : adds the value to the last index as single item value

number_List.append(1000)
print(number_List)

number_List.append([2000, 3000])  # now we are appending the list ,
# but it will append the list as single value O/P: [100,200,300,400,500,1000,[2000,3000]]
print(number_List)

number_List.append("GOA")  # Since List as Mutable
print(number_List)

# Extend : Adds the Value to the List as multiple item value

number_List.extend("123")
print(number_List)

# insert : insert the value at specific index

number_List.insert(2, "Kabira")
print(number_List)

# Delete : Delete Specific Index Value

del number_List[-5]  # Delete the [2000,3000] List
print(number_List)

del number_List[-4]
print(number_List)

# remove : removes the value without index

number_List.remove("Kabira")
print(number_List)

number_List.remove('1')
number_List.remove('2')
number_List.remove('3')
print(number_List)

# pop : by default removes the last index value

number_List.pop()
print(number_List)

# clear : clears the list and make it empty
number_List.clear()
print(number_List)

number_List= [100, 200, 300, 400, 500]
print(number_List)

print(max(number_List))
print(min(number_List))
print(sorted(number_List)) # Ascending Order ( sorted will create new List)
print(sorted(number_List,reverse=True)) # Descending Order
print(number_List)
number_List.sort() # sort() will change the original list
print(number_List)
number_List.sort(reverse=True) #
print(number_List)