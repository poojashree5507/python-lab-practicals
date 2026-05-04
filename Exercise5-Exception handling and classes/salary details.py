class employee:
    def __init__(self):
        self.name =[]
        self.gross_pays=[]
        self.salaries= []
    def get_name(self):
        n=int(input("enter the number of employees:"))
        for i in range(n):
            names=input(f"Enter name of employee{i+1}:")
            self.name.append(names)
    def get_salary(self):
        for i in range(len(self.name)):
          s=int(input(f"Enter salary of employee{i+1}:"))
          self.salaries.append(s)
    def salary(self):
        self.gross_pays = []
        for s in self.salaries:
            da = 0.10 * s
            hra = 0.20 * s
            gross = s + hra + da
            self.gross_pays.append(gross)

    def display(self):
        print("...Employee Details...")
        for i in range (len(self.name)):
            print("Name:",self.name[i])
            print("Salary:",self.gross_pays[i])

emp=employee()
emp.get_name()
emp.get_salary()
emp.salary()
emp.display()
