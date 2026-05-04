a=int(input("Enter your age:"))
if a>=18:
    print("You are eligible for voting.")
elif a<18 and a>0:
    print("You are not eligible for voting.")
else:
    print("Invalid age.Enter proper age")
