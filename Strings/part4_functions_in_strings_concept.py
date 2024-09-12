# Common Functions Or Pre-Defined Functions in Python
from audioop import reverse

city = "Hyderabad is Beautiful city"

print(len(city))  # prints length
print(max(city))  # based on ascii values , prints the max character
print(min(city))  # based on ascii values, prints the min character
a = sorted(city)  # returns the list and prints in ascending order
print(a)
b = sorted(city, reverse=True)  # returns the list and prints in descending order
print(b)

print(city.capitalize())  # Prints first char in Captial and others in small
print(city.title())  # Prints first char in all words as  Captial and others in small
print(city.upper())
print(city.lower())
print(city.swapcase())  # converts the letter which is in Caps to Small and vice versa.

print(city.count("au"))  # prints the frequency of characters or SubStrings in a string

print(city.find("i"))  # prints the character index position
print(city.find("au"))  # we can pass any substring as well
print(city.find("x"))  # which is not present in string or substring prints -1

print(city.index("it"))  # prints the character index position
# print(city.index("wasd")) # throws an error substring not found




print(city.startswith("ahd"))  # False
print(city.startswith("Hyd"))  # True
print(city.endswith("addkey"))  # False
print(city.endswith("ty"))  # True

print(city.split(" "))
print(city.split("i"))

print("-".join(city))  # join with '-' in all the characters

print(city.isalnum())  # False
print(city.isupper())  # False

print(city.replace("Hyderabad", "Jaipur"))
print("   Hi My Name Is Kabira                ".strip())  # removes the Trailing and Leading Spaces
print("               Hi My Name Is Kabira".lstrip())   # removes the Trailing Spaces
print("Hi My Name Is Kabira                                     ".lstrip())    # removes the Leading Spaces
