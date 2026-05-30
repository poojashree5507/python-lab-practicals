class word:
    def __init__(self, a):
        self.a = a
    def __eq__(self, other):
        return self.a == other.a
    def __add__(self, other):
        return self.a + other.a
a=input("Enter a word: ")
b=input("Enter another word: ")
w=word(a)
w1=word(b)
print("compare:",w==w1)
print("concatenate:",w+w1)
