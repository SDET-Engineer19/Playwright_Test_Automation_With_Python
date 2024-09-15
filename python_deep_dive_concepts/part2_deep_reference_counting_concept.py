import sys

w1 = 9191
l = w1
m = l

# Verify l & m values
print(w1)
print(l)
print(m)

print("####################")

# verify the id of k,l,m : should be same

print(id(w1))
print(id(l))
print(id(m))

print("######## GET THE MEMORY ADDRESS #########")
print(sys.getrefcount(w1))  # get the memory address
