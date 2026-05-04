#to check weird or not

a=int(input("Enter a:"))
if a%2==1:
   print("...Weird...")
else:
   if a>=0 and a<=20:
      print("...Not weird...")
   elif a>=21 and a<=40:
      print("...Weird...")
   else:
      print("...Not weird...")
