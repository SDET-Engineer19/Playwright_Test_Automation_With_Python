# using for loop:
def reverse_string(a):
    temp = " "
    for key in a:
        temp = key + temp
    return temp


name = "Kabira"
val = reverse_string(name)
print("####### Using For Loop #######")
print(val)

# using string pre defined methods:
print("####### Using Pre Defined Methods #######")
print(name[::-1])
