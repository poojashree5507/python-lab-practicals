class Vehicle:
    def __init__(self):
        self.make = None
        self.year=0
        self.colour=""
    def getdetails(self):
        self.make=input("Enter make details: ")
        self.year=input("Enter year: ")
        self.colour=input("Enter colour: ")
    def display(self):
        print("Vehicle Details")
        print(f"Make:{self.make}|Year: {self.year}|Colour: {self.colour}")
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.model=""
        self.capacity=0
    def getcardetails(self):
        self.model=input("Enter model: ")
        self.capacity=input("Enter capacity: ")
    def displaycar(self):
        print("Car Details")
        print(f"Model:{self.model}|Capacity:{self.capacity}")
class Bike(Vehicle):
    def __init__(self):
        super().__init__()
        self.type=""
        self.m=""
    def getbikedetails(self):
        self.type=input("Enter type: ")
        self.m=input("Enter Mileage: ")
    def displaybike(self):
        print("Bike Details")
        print(f"Type:{self.type}|Mileage:{self.m}")
print("Enter car details:")
c=Car()
c.getdetails()
c.getcardetails()
print("Enter bike details:")
b=Bike()
b.getdetails()
b.getbikedetails()
print("...Car and Bike details ...")
c.display()
c.displaycar()
b.display()
b.displaybike()
