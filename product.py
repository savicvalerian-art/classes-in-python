class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        
    def check_quantity(self):
        if self.quantity < 10:
            return False
        else:
            return True
        
# Primer korišćenja
product1 = Product(
    "Laptop",
    999.99,
    5,
    "Gaming laptop sa 16GB RAM memorije"
)

print(product1.check_quantity())