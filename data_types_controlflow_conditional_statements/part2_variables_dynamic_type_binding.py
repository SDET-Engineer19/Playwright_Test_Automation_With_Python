# Variables and Dynamic Typing
# where declaration of variable type(Like Integer,String etc) is not required in Python
from imaplib import Flags

a = 10
name = "Kabira"

flag = True

print(a)
print(name)
print(flag)

print(type(a))
print(type(name))
print(type(flag))

# Dynamic Binding : Storing the multiple value for one variable name
c = "Tom"
c = 3
c = False

print(c)

# Special Variables
d = 3; e = 4; f = 5;
print(d)
print(e)
print(f)

d , e ,f = 5,6,7
print(d)
print(e)
print(f)

d = e = f = 10
print(d)
print(e)
print(f)
