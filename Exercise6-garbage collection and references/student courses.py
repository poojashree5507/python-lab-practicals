import sys

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.courses = []

    class Course:
        def __init__(self, cname):
            self.cname = cname

    def add_course(self, cname):
        self.courses.append(Student.Course(cname))

    def display(self):
        print(f"\nStudent: {self.name} (Roll: {self.roll})")
        print("Courses:", ", ".join(c.cname for c in self.courses) or "None")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
s = Student(name, roll)

n = int(input("How many courses to enroll? "))
for _ in range(n):
    s.add_course(input("Enter course name: "))

s.display()
print("\nReference count for 's':", sys.getrefcount(s) - 1)
t = s
print("After creating another reference:", sys.getrefcount(s) - 1)
del t
print("After deleting the extra reference:", sys.getrefcount(s) - 1)
