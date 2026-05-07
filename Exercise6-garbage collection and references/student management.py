import sys
import gc
class University:
    def __init__(self, university_name):
        self.university_name = university_name
        self.students = []

    class Student:
        def __init__(self, rollno, name, university):
            self.rollno = rollno
            self.name = name
            self.university = university

        def display_details(self):
            print(f"Roll No: {self.rollno}, Name: {self.name}, University: {self.university.university_name}")

        def __del__(self):
            print(f"Student object with Roll No {self.rollno} is being deleted from memory.")

    def add_student(self, rollno, name):
        student = self.Student(rollno, name, self)
        self.students.append(student)
        print(f"Student {name} added successfully.")
        print(f"Reference count for this student: {sys.getrefcount(student) - 1}")

    def remove_student(self, rollno):
        for student in self.students:
            if student.rollno == rollno:
                print(f"Removing student {student.name}...")
                print(f"Reference count before removal: {sys.getrefcount(student) - 1}")
                self.students.remove(student)
                del student
                gc.collect()
                return
        print("Student not found.")

    def display_all(self):
        if not self.students:
            print("No students enrolled.")
        else:
            print("\nList of Students:")
            for student in self.students:
                student.display_details()
                print(f"Current reference count: {sys.getrefcount(student) - 1}")


if __name__ == "__main__":
    gc.enable()

    uni_name = input("Enter University Name: ")
    university = University(uni_name)

    while True:
        print("\n1. Add Student")
        print("2. Remove Student")
        print("3. Display All Students")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            rollno = input("Enter Roll No: ")
            name = input("Enter Name: ")
            university.add_student(rollno, name)

        elif choice == "2":
            rollno = input("Enter Roll No to remove: ")
            university.remove_student(rollno)

        elif choice == "3":
            university.display_all()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")
