import gc

class Employee:
    class Address:
        def __init__(self, street, city, pincode):
            self.street, self.city, self.pincode = street, city, pincode
        def __str__(self):
            return f"{self.street}, {self.city} - {self.pincode}"

    def __init__(self, name, emp_id, dept, street, city, pincode):
        self.name, self.emp_id, self.dept = name, emp_id, dept
        self.address = Employee.Address(street, city, pincode)
        print(f"[Hired] {self.name}")

    def display(self):
        print(f"Name: {self.name}\nID: {self.emp_id}\nDept: {self.dept}\nAddress: {self.address}")

    def __del__(self):
        print(f"[Resigned] {self.name} (Object deleted)")
employees = []
n = int(input("Enter number of employees to hire: "))

for _ in range(n):
    name = input("Name: ")
    emp_id = input("ID: ")
    dept = input("Department: ")
    street = input("Street: ")
    city = input("City: ")
    pincode = input("Pincode: ")
    employees.append(Employee(name, emp_id, dept, street, city, pincode))

print("\n--- Employee Details ---")
for emp in employees:
    emp.display()

resign_index = int(input("\nEnter employee index to resign (0-based): "))
if 0 <= resign_index < len(employees):
    employees[resign_index] = None
    gc.collect()

print("\nRemaining Employees:")
for emp in employees:
    if emp:
        emp.display()
