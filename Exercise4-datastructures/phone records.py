m={}
n=int(input("Enter number of records: "))
for i in range(n):
    num=int(input("Enter number: "))
    name=input("Enter name: ")
    m[num]=name
search=int(input("Enter number to search: "))
if search in m:
    print("Name:",m[search])
else:
    print("Number not found")
