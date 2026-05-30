import csv
file = open("employee.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(["Emp_id", "Name", "Basic_Pay"])
n = int(input("Enter number of employees: "))
for i in range(n):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    basic = int(input("Enter Basic Pay: "))
    writer.writerow([emp_id, name, basic])
file.close()
file = open("employee.csv", "r")
reader = csv.reader(file)
next(reader)
for row in reader:
    total_salary = int(row[2]) + 5000
    print("\nEmployee ID :", row[0])
    print("Employee Name :", row[1])
    print("Total Salary :", total_salary)
file.close()
