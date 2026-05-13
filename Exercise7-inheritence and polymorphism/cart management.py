class Product:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.p_id = 0

    def getdetails(self):
        self.p_id = int(input("Enter product id: "))
        self.name = input("Enter product name: ")
        self.price = int(input("Enter product price: "))

    def add_to_cart(self):
        print(f"{self.name} added to cart successfully")

    def display(self):
        print("\n...product details...")
        print(f"Name: {self.name} | Product ID: {self.p_id} | Price: {self.price}")

class Electronics(Product):
    def __init__(self):
        super().__init__()
        self.brand = ""
        self.warrenty = ""

    def getedetails(self):
        # We use the name already captured in getdetails or prompt again
        self.brand = input("Enter brand: ")
        self.warrenty = input("Enter warranty: ")

    def display(self):
        super().display()
        print(f"Brand: {self.brand} | Warranty: {self.warrenty}")

class Clothing(Product):
    def __init__(self):
        super().__init__()
        self.type = ""
        self.size = ""
        self.colour = ""

    def getcloth(self):
        self.type = input("Enter type of clothing: ")
        self.size = input("Enter size of clothing: ")
        self.colour = input("Enter colour of clothing: ")

    def display(self):
        super().display()
        print(f"Type: {self.type} | Size: {self.size} | Colour: {self.colour}")
cart = []

print("--- Enter Electronic Details ---")
e = Electronics()
e.getdetails()
e.getedetails()
e.add_to_cart()
cart.append(e)

print("\n--- Enter Clothing Details ---")
c = Clothing()
c.getdetails()
c.getcloth()
c.add_to_cart()
cart.append(c)

print("\n...Cart Details...")
for item in cart:
    item.display()
