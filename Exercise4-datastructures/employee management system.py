n= int(input("Enter number of employees: "))
emp_list = []
for i in range(n):
    eid = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    salary = int(input("Enter Salary: "))
    emp = (eid, name, salary)
    emp_list.append(emp)
employees = tuple(emp_list)
print("\nEmployee Records:")
for e in employees:
    print(e)
search_id = int(input("\nEnter Employee ID to search: "))
found = False
for e in employees:
    if e[0] == search_id:
        print("Employee Found:", e)
        found = True
        break
if not found:
    print("Employee not found")
highest = employees[0]
for e in employees:
    if e[2] > highest[2]:
        highest = e
print("\nEmployee with Highest Salary:", highest)
print("\nEmployees with Salary greater than 50000:")
for e in employees:
    if e[2] > 50000:
        print(e)
