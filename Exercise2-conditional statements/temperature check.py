print("temperature:")
print("warm-w , cold-c")
print("humidity:")
print("dry-d , humid-h")
a=input("enter temperature:")
b=input("enter humidity:")
if a=="w":
    if b=="d":
        print("Play Basketball")
    else:
        print("Play Tennis")
elif a=="c":
    if b=="d":
        print("Play Cricket")
    else:
        print("Swim")
else:
    print("Wrong Input")
