class Students:
    def __init__(self):
        self.names = []
        self.marks = []

    def get_names(self):
        n = int(input("Enter number of students: "))
        for i in range(n):
            name = input(f"Enter name for student {i+1}: ")
            self.names.append(name)

    def get_marks(self):
        for i in range(len(self.names)):
            print(f"\nEnter marks for {self.names[i]}:")
            student_marks = []
            for j in range(5):
                mark = int(input(f"  Enter mark {j+1}: "))
                student_marks.append(mark)
            self.marks.append(student_marks)

    def display_results(self):
        print("\n--- Final Results ---")
        for i in range(len(self.names)):
            avg = sum(self.marks[i]) / len(self.marks[i])
            grade = self.get_grade(avg)
            print(f"Student: {self.names[i]} | Average: {avg:.2f} | Grade: {grade}")

    def get_grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

s = Students()
s.get_names()
s.get_marks()
s.display_results()
