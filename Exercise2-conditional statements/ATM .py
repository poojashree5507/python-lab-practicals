a=float(input("enter your current balance:"))
print(" 1:deposit, 2:withdrawal")
b=int(input("enter the type of transaction-"))
c=float(input("enter the transaction amount:"))
if b==1:
   if c>=1000:
      s=a+c
      print("Updated balance is",s)
   else:
      print("This amount can not be deposited->min deposition amount is not sufficient")
elif b==2:
   if a-c<1000:
      print("This amount can not be withdrawn->min balance is not sufficient")
   else:
      d=a-c
      print("Updated balance is",d)
else:
   print("Invalid choice is given")
