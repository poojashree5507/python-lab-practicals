import math
a=float(input("Enter a number-a: "))
b=float(input("Enter a number-b: "))
c=float(input("Enter a number-c: "))
d=(b**2-4*a*c)
if d>0:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("The roots are:",r1,r2)
elif d==0:
    r1=-b/(2*a)
    r2=-b/(2*a)
    print("The roots are:",r1,r2)
else:
    print("No real roots")
