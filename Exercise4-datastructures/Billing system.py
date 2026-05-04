a=int(input("Enter number of elements: "))
items=[]
def get_items(n):
    for i in range(n):
        n=input("Enter name:")
        q=int(input("enter quantity:"))
        p=float(input("enter price:"))
        items.append((n,p,q))
    return items
st=[]
def s_t(items):
    for i in range(len(items)):
        s=items[i][1]*items[i][2]
        st.append(s)
    return s_t
def tot(l):
    t=0
    t=sum(st)
    print("SubTotal:",t)
    if t>3000:
        discount=t*0.1
        t=t-discount
        print("bill after discount",t)
    else:
        discount=0
        t=t+discount
        print("bill after discount",discount)
    c=t*0.05
    t=t+c
    print("GST is",c)
    print("final amount is",t)
m=get_items(a)
print("Items:",m)
sub=s_t(m)
tot(sub)
