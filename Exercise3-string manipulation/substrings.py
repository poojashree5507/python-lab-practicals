a=input("enter a string:")
n=len(a)
for i in range(n):
    for j in range (i+1,n+1):
        print(a[i:j])
