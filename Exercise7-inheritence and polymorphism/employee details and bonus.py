class employee:
    def getdetails(self):
        self.ID=int(input("Enter Employee ID:"))
        self.name=input("Enter Employee Name:")
        self.salary=float(input("Enter Employee Salary:"))
        self.percentage=float(input("Enter Employee Percentage:"))
    def calculate_bonus(self):
        bonus=(self.salary*self.percentage)/100
        print("Bonus:",bonus)
class manager(employee):
    def managerdetails(self):
        self.department=input("Enter department:")
        self.team_size=int(input("Enter team size:"))
        self.allowance=float(input("Enter allowance:"))
    def printmanager(self):
        print("\n Manager Details:")
        print("ID:",self.ID)
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)
        print("Team size:",self.team_size)
        print("Allowance:",self.allowance)
        self.calculate_bonus()
class developer(employee):
    def developerdetails(self):
        self.project=input("Enter project name:")
        self.experience=input("Enter experience details:")
    def printdeveloper(self):
        print("Project Details:")
        print("ID:",self.ID)
        print("Name:",self.name)
        print("salary:",self.salary)
        print("Project:",self.project)
        print("Experience:",self.experience)
        self.calculate_bonus()
print("Enter Manager Details:")
m=manager()
m.getdetails()
m.managerdetails()
print("\n Enter developer Details:")
d=developer()
d.getdetails()
d.developerdetails()
print("---------Output--------")
m.printmanager()
d.printdeveloper()
