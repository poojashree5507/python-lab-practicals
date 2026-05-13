class Department:
    def __init__(self):
        self.id=0
        self.name=""
    def getdep(self):
        self.id=int(input("Enter department id:"))
        self.name=input("Enter department name:")
    def printdep(self):
        print(f"Department Name: {self.name}|department ID: {self.id}")
class course(Department):
    def __init__(self):
        super().__init__()
        self.code=""
        self.cname=""
        self.d=""
    def getcourse(self):
        self.code=input("Enter course code:")
        self.cname=input("Enter course name:")
        self.d=input("Enter course duration(months):")
    def printcourse(self):
        print("course details")
        print(f"Course Code: {self.code}|Course Name: {self.cname}|Course Duration: {self.d} months")
class student(course):
    def __init__(self):
        super().__init__()
        self.rn=0
        self.sname=""
        self.marks=0
    def getstudent(self):
        self.rn=int(input("Enter student Roll number:"))
        self.sname=input("Enter student name:")
        self.marks=list(map(int,input("Enter student marks:").split()))
    def printstudent(self):
        print("student details")
        print(f"Student Name:{self.sname}|Roll number:{self.rn}|Student Marks:{self.marks}")
a=student()
a.getdep()
a.getcourse()
a.getstudent()
a.printdep()
a.printcourse()
a.printstudent()
