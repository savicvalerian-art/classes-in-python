from product import Product

class User:
    def __init__(self, name, username, email, phone, address):
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.address = address
        self.shopping_history = []
        
    def check_email(self):
        if "@" in self.email:
            return True
        else:
            return False
        
    def total_spent(self):
        ukupno = 0

        for product in self.shopping_history:
            ukupno += product.price

        return ukupno
        
    def add_product(self, product:Product):
        self.shopping_history.append(product)
        
# Primer korišćenja
product1 = Product(
    "Laptop",
    1200.50,
    5,
    "Gaming laptop"
)

product2 = Product(
    "Mouse",
    25.99,
    50,
    "Wireless mouse"
)

user1 = User(
    "Petar Petrovic",
    "petar123",
    "petar@gmail.com",
    "061234567",
    "Novi Sad"
)

print(user1.check_email())  # True

user1.add_product(product1)
user1.add_product(product2)

print(user1.total_spent())  # 1226.49