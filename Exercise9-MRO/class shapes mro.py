import math


class Shapes:
    def calculate_area(self):
        print("Area calculation")

    def calculate_perimeter(self):
        print("Perimeter calculation")


class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = math.pi * self.radius * self.radius
        print("Area of Circle =", area)

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("Perimeter of Circle =", perimeter)


class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        area = self.length * self.breadth
        print("Area of Rectangle =", area)

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print("Perimeter of Rectangle =", perimeter)


class Triangle(Shapes):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        print("Area of Triangle =", area)

    def calculate_perimeter(self):
        perimeter = self.a + self.b + self.c
        print("Perimeter of Triangle =", perimeter)


c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(3, 4, 5)

c.calculate_area()
c.calculate_perimeter()

print()

r.calculate_area()
r.calculate_perimeter()

print()

t.calculate_area()
t.calculate_perimeter()

print("\nMRO Tracing")
print("Circle MRO:", Circle.mro())
print("Rectangle MRO:", Rectangle.mro())
print("Triangle MRO:", Triangle.mro())
