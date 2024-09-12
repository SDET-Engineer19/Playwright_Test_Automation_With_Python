from symbol import break_stmt

cars = ["Audi", "Benz", "BMW"]
print(cars)

print(cars[0])
print(cars.__len__())
cars.insert(3, "Volvo")
print(cars)

cars.pop(1) # removes the specified index value
print(cars)

cars.append('Benz')
print(cars)
## Iterate Array
for car in cars:
    if car.__eq__("A1"):
        break
    else:
        print("No Such Value")

print("Came Out of the Loap")
