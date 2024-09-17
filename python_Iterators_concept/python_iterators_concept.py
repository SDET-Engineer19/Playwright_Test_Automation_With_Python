# Iteration  : Process of traversing one-by-one item of an object
# Iterator :  iterator is an object which traverse through sequence of data and which helps iteration
# Iterable : User can perform iteration on object

# Verify the memory using iterator

# 1. Example using for loop to check the memory of list
import sys

from arrays_development_Practice.basic_concept_of_ArrayMethods import numbers

L1 = [x for x in range(1, 100000)]

# for x in L1:
#  print(x*2)


# 2. Using Range function

y = range(1, 100000)

#  for k in y:
#   print(k*2)

print("Memory Size : ", sys.getsizeof(L1) / 1024)

print("Memory Size : ", sys.getsizeof(y) / 1024)

L = [1, 2, 3, 4, 5]
print(L)
print(type(L))  # List

# L is an iterable
print(type(iter(L)))  # iter(L) is iterator

# Important tricks to understand
# 1. Every Iterable has an iter function
# 2. Every Iterator has both iter and next function

# Example for 1 :
# first iterate using loop : if is iterate then it is iterable
a = 100
# verify a is iterable or not
# so we cannot iterate a using loop, so it is not iterable
# second method : using dir function, if it has __iter__ function then it is iterable
check_iterable = dir(a)
print(check_iterable)  # there is no __iter__ function

# Example 2 :
num_tuples = (100, 200, 300, 400, 500)
print(num_tuples)

check_iterable = dir(num_tuples)
print(check_iterable)  # so num_tuples is an iterable

L2 = ["Playwright", "Selenium", "Cypress"]
print(L2)

check_iterable = dir(L2)
print(check_iterable)  # so L2 is an iterable

# To verify if any object has iter and next function

name_tuples = ("Kabira", "Tom", "Peter", "Mark")

print(dir(iter(name_tuples)))  # it is an iterator which has both next and iter functions

course_details = ["Kubernetes", "Docker", "DSA", "Playwright"]

print(dir(iter(course_details)))

cert_details_dict = {"k8:CKA", "Automation:Playwright", "Orchestration:Docker"}
print(cert_details_dict)
print(dir(iter(cert_details_dict)))

# To check how for loop works

num = [1, 2, 3]

iter_num = iter(num)

print(next(iter_num))
print(next(iter_num))
print(next(iter_num))


# print(next(iter_num))


# Making my own loop

def my_own_loop(iterable):
    iterator = iter(iterable)

    while True:

        try:
            print(next(iterator))
        except StopIteration:
            break


a = [1, 2, 3]
b = (100, 200, 300, 400)
c = {1000, 2000, 3000, 4000}
d = {"name:Kabira","age:37"}


my_own_loop(a)
my_own_loop(b)
my_own_loop(c)
my_own_loop(d)