a=input("Enter a string:")
vowels="aeiouAEIOU"
v=0
c=0
for ch  in a:
    if ch.isalpha():
        if ch in vowels:
            v=v+1
        else:
            c=c+1
print("vowels is",v)
print("consonants is",c)
