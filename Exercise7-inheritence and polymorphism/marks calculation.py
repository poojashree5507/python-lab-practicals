
class student:
    def __init__(self):
        self.name=""
        self.rollno=0
        self.testmark=0
    def getdetails(self):
        self.name=input("Enter student name:")
        self.rollno=int(input("Enter roll no:"))
        self.testmark=float(input("Enter test mark:"))
    def total_mark(self):
        return self.testmark
    def display(self):
        print("\nStudent Details:")
        print("Name:",self.name)
        print("Roll no:",self.rollno)
        print("Testmark:",self.testmark)
class litrary(student):
    def __init__(self):
        super().__init__()
        self.litrary_mark=0
    def get_litrary(self):
        self.litrary_mark=float(input("Enter litrary mark:"))
    def total_mark(self):
        return self.testmark+self.litrary_mark
    def display(self):
        super().display()
        print("Litrary mark:",self.litrary_mark)
class sports_students(student):
    def __init__(self):
        super().__init__()
        self.sports_mark=0
    def get_sports_students(self):
        self.sports_mark=float(input("Enter sports mark:"))
    def total_mark(self):
        return self.testmark+self.sports_mark
    def display(self):
        super().display()
        print("Sports mark:",self.sports_mark)
class litrary_sports_students(litrary,sports_students):
    def total_mark(self):
        return self.testmark+self.sports_mark+self.litrary_mark
    def display(self):
        super().display()
        print("sports marks:",self.sports_mark)
print("\nStudent Details:")
o=litrary_sports_students()
o.getdetails()
o.get_litrary()
o.get_sports_students()
print("\n output:")
o.display()
print("Total marks:",o.total_mark())
