a = 4
b = 4

# Same values and Same Memory Location

print(a is b)

c = 10
d = 19
print(c is d)

# Different Value and Different Memory Location

x = [1,2,3]
y = [1,2,3]

print(x is y) # Same List Value and Different Memory Location

x = "Hyderabad is a Beautiful City"
y = [1,2,3]

print(x is y) # Different Data type Value and Different Memory Location

m = "hello-kabira"
p  = "hello-kabira"

print(m is p)  # Same values and Same Memory Location

