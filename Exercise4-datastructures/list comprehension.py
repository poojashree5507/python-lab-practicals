l=[1,2,3]
while True:
    print("1.Insert at position")
    print("2.append element")
    print("3.compare lists")
    print("4.print id of element")
    print("5.find first occurence")
    print("6.exit")
    c=int(input("Enter your choice:"))
    if c==1:
        p= int(input("Position:"))
        v= int(input("Value:"))
        l.insert(p,v)
        print(l)
    elif c==2:
        v= int(input("Value:"))
        l.append(v)
        print(l)
    elif c==3:
        l2=list(map(int,input("Enter second list:").split()))
        print("equal"if l2==l else "not equal")
    elif c==4:
        for i in l:
            print(i,"ID:",id(i))
    elif c==5:
        q=int(input("enter element:"))
        if q in l:
            print(l.index(q))
    elif c==6:
        break
else:
    print("Enter a valid choice")
