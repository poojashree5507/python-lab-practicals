class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] + other.values[i])

        return Vector(result)

    def __sub__(self, other):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] - other.values[i])

        return Vector(result)

    def __mul__(self, scalar):
        result = []

        for i in range(len(self.values)):
            result.append(self.values[i] * scalar)

        return Vector(result)

    def __eq__(self, other):
        return self.values == other.values

    def dot_product(self, other):
        total = 0

        for i in range(len(self.values)):
            total += self.values[i] * other.values[i]

        return total

    def cross_product(self, other):
        a1, a2, a3 = self.values
        b1, b2, b3 = other.values

        result = [
            (a2 * b3 - a3 * b2),
            (a3 * b1 - a1 * b3),
            (a1 * b2 - a2 * b1)
        ]

        return Vector(result)

    def display(self):
        print(self.values)

n = int(input("Enter size of vector: "))

print("Enter elements of Vector A:")
A_values = list(map(int, input().split()))

print("Enter elements of Vector B:")
B_values = list(map(int, input().split()))

A = Vector(A_values)
B = Vector(B_values)

print("\nVector Addition:")
(A + B).display()

print("\nVector Subtraction:")
(A - B).display()

scalar = int(input("\nEnter scalar value: "))
print("Scalar Multiplication:")
(A * scalar).display()

print("\nEquality Check:")
print(A == B)

print("\nDot Product:")
print(A.dot_product(B))

if n == 3:
    print("\nCross Product:")
    (A.cross_product(B)).display()
else:
    print("\nCross Product is only defined for 3D vectors.")
