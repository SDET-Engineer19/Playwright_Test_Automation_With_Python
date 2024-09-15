value = "Hello World"
print(len(value))

# Positive Indexing : Starts from Left to Right

print(value[0])
print(value[2])

# Negative Indexing: Starts from Right to Left
print(value[-1])
print(value[-4])

# Slicing: can skip the characters , by passing indexing
print(value[1:5])  # ello
print(value[2:9])

print(value[0:10:2]) # H l o W r d
# H e l l o W o r l d : H l o o l

print(value[2:8:3])
# H e l l o W o r l d : l W

print(value[1:9:3])
# H e l l o W o r l d :  e o  r

# Slicing with Negative Numbers

print(value[-1:-5:-2])
# W o r l d H e l l o  :  d r
print(value[-1:-9:-2])
# W o r l d H e l l o  : d r W l
print(value[-1:-8:-3])
# W o r l d H e l l o  : d o l

print(value[-1:-7:-2])
# W o r l d H e l l o  : d r W

print(value[::-1])