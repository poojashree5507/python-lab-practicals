class Supplier:
    count = 0
    def __init__(self, name, contact):
        self.name, self.contact = name, contact
        Supplier.count += 1

class Product:
    count = 0
    class Specification:
        def __init__(self, color, weight):
            self.color, self.weight = color, weight

    def __init__(self, name, price, supplier, color, weight):
        self.name, self.price, self.supplier = name, price, supplier
        self.spec = Product.Specification(color, weight)
        Product.count += 1

    def display(self):
        print(f"\nProduct: {self.name}\nPrice: ${self.price}\n"
              f"Color: {self.spec.color}, Weight: {self.spec.weight}kg\n"
              f"Supplier: {self.supplier.name} ({self.supplier.contact})")

products, suppliers = [], []

n_sup = int(input("Enter number of suppliers: "))
for _ in range(n_sup):
    suppliers.append(Supplier(input("Supplier name: "), input("Contact: ")))

n_prod = int(input("\nEnter number of products: "))
for _ in range(n_prod):
    name = input("Product name: ")
    price = float(input("Price: "))
    sup_idx = int(input(f"Supplier index (0-{len(suppliers)-1}): "))
    color = input("Color: ")
    weight = float(input("Weight (kg): "))
    products.append(Product(name, price, suppliers[sup_idx], color, weight))

print("\n--- Inventory ---")
for p in products:
    p.display()
print(f"\nTotal Products: {Product.count}, Total Suppliers: {Supplier.count}")
