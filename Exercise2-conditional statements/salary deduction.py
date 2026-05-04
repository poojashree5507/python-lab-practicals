a=float(input("Enter your monthly salary:"))
b=int(input("Enter number of leave days:"))
if b<=2:
   print("your salary is",a)
else:
   s=a-(b-2)*500
   print("your salary is",s)
