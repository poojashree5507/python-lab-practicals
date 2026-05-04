def add1(a,b):
    return a+b
def sub2(a,b):
    return a-b
def mult3(a,b):
    return a*b
def div4(a,b):
    if  b==0:
        print("not possible..")
    else:
        return a/b
def mod5(a,b):
    return a%b
print("...Simple Calculator...")
print("1-add")
print("2-sub")
print("3-mul")
print("4-div")
print("5-mod")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("Enter your choice:"))
if c==1:
    print("Result:",add1(a,b))
elif c==2:
    print("Result:",sub2(a,b))
elif c==3:
    print("Result:",mult3(a,b))
elif c==4:
    print("Result:",div4(a,b))
elif c==5:
    print("Result:",mod5(a,b))
else:
    print("Invalid Choice")
