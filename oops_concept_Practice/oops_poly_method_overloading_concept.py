class Geometry:

    # Overloading

    def area(self, a, b=0):
        if b == 0:
            return "Circle: ", 3.14 * a * a
        else:
            return "Rect: ", a * b


obj = Geometry()
print(obj.area(2, 12))
print(obj.area(12))

