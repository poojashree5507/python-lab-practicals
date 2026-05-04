class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    def display(self):
            print("Name:",self.name)
            print("Employee ID:",self.emp_id)
            print("Salary:",self.salary)
n=int(input("enter the number of employees:"))
employees=[]
for i in range(n):
    name=input("Name:")
    emp_id=int(input("Employee ID:"))
    salary=float(input("Salary:"))
    employees.append(Employee(name,emp_id,salary))
print("...Employee Details...")
for e in employees:
    e.display()
search_id=int(input("Enter Employee ID to search:"))
f=0
for e in employees:
    if e.emp_id==search_id:
            f=f+1
            print("Name:",e.name)
            break
if f==0:
    print("Employee not found")
max_e=employees[0]
for e in employees:
    if e.salary>max_e.salary:
         max_e=e
print("Employee with highest salary:",max_e.name)
max_e.display()
