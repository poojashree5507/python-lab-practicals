tele={}
n=int(input("Enter number of contacts: "))
for i in range(n):
    name=input("Enter name: ")
    number=int(input("Enter number: "))
    tele[name]=number
print("...telephone directory...")
for i in tele:
    print(i,":",tele[i])
