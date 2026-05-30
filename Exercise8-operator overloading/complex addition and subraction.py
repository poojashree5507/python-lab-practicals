class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return complex((self.x + other.x),(self.y + other.y))
    def __sub__(self, other):
        return complex((self.x - other.x),(self.y - other.y))
x=int(input("Enter real part: "))
y=int(input("Enter imaginary part: "))
x1=int(input("Enter real part: "))
y1=int(input("Enter imaginary part: "))
v1=Complex(x,y)
v2=Complex(x1,y1)
v3=v1+v2
v4=v1-v2
print("addition:",v3)
print("subtraction:",v4)
