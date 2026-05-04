s=input("Enter a password:")
has_digit=False
has_lower=False
has_upper=False
has_special=False
has_space=False
if len(s)<8 or len(s)>15:
    print("invalid password")
else:
    for ch  in s:
        if ch == " ":
            has_space=True
        elif ch in "1234567890":
            has_digit=True
        elif ch>="a" and ch<="z":
            has_lower=True
        elif ch>="A" and ch<="Z":
            has_upper=True
        elif ch in "!@#$%^&*()":
            has_special=True
    if( not has_space and has_digit and has_lower and  has_upper and  has_special ):
        print("valid password")
    else:
        print("invalid password")
