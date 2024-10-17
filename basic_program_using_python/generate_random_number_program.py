import random

value = random.randint(10, 20)

a = int(input("Enter New Value : "))
counter = 1
while a != value:
    if a < value:
        print("Guess Higher Value ")
    else:
        print("Guess Lower Value ")

    a = int(input("Enter New Value : "))
    counter += 1

print("Correct Guess and took ", counter, " attempts")
