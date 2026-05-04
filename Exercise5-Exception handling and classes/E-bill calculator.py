class EB:
    def __init__(self):
        self.u=u
        self.bill=0
    def calculate(self):
        if self.u<=100:
            self.bill=0
        elif self.u<=200 and self.u>100:
            self.bill=(self.u-100)*1.5
        elif self.u<=300 and self.u>200:
            self.bill=(self.u-200)*2.5+(100*1.5)
        elif self.u<=400 and self.u>300:
            self.bill=(100*1.5)+(100*2.5)+(self.u-300)*4
        else:
            self.bill=(100*1.5)+(100*2.5)+(100*4)+(self.u-400)*5
    def display(self):
        print("Units:",self.u)
        print("Bill:",self.bill)
u=int(input("Enter your units:"))
units=EB()
units.calculate()
units.display()
