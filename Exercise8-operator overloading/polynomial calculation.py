class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = coeffs
    def __mul__(self, other):
        result = [0] * (len(self.coeffs) + len(other.coeffs) - 1)

        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                result[i + j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(result)

    def display(self):
        degree = len(self.coeffs) - 1
        terms = []

        for i, coeff in enumerate(self.coeffs):
            power = degree - i

            if power > 1:
                terms.append(f"{coeff}x^{power}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}")

        return " + ".join(terms)

n1 = int(input("Enter number of coefficients for Polynomial 1: "))
c1 = list(map(int, input("Enter coefficients: ").split()))

n2 = int(input("Enter number of coefficients for Polynomial 2: "))
c2 = list(map(int, input("Enter coefficients: ").split()))

p1 = Polynomial(c1)
p2 = Polynomial(c2)

p3 = p1 * p2

print("Polynomial 1 :", p1.display())
print("Polynomial 2 :", p2.display())
print("Multiplication :", p3.display())
