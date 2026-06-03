from product import Product
from employee import Employee
from user import User

# =========================
# Kreiranje proizvoda
# =========================
products = [
    Product("Laptop", 1200.0, 5, "Gaming laptop"),
    Product("Mouse", 25.5, 100, "Wireless mouse"),
    Product("Keyboard", 75.0, 50, "Mechanical keyboard"),
    Product("Monitor", 300.0, 8, "27 inch monitor"),
    Product("USB Cable", 10.0, 200, "Type-C USB cable")
]

# =========================
# Kreiranje zaposlenih
# =========================
employees = [
    Employee(
        "Marko Markovic",
        "marko@gmail.com",
        80000,
        "Beograd"
    ),
    
    Employee(
        "Jelena Jovanovic",
        "jelena@gmail.com",
        90000,
        "Novi Sad"
    )
]

# =========================
# Kreiranje korisnika
# =========================
users = [
    User(
        "Petar Petrovic",
        "petar123",
        "petar@gmail.com",
        "061111111",
        "Nis"
    ),
    
    User(
        "Ana Anic",
        "ana99",
        "ana@gmail.com",
        "062222222",
        "Kragujevac"
    ),
    
    User(
        "Nikola Nikolic",
        "nikola007",
        "nikola@gmail.com",
        "063333333",
        "Subotica"
    )
]

# =========================
# Demonstracija Product klase
# =========================
print("=== PRODUCT ===")

for product in products:
    print(f"\nNaziv: {product.name}")
    print(f"Cena: {product.price}")
    print(f"Kolicina: {product.quantity}")
    print(f"Opis: {product.description}")
    print(f"Dovoljno na stanju: {product.check_quantity()}")
    
# =========================
# Demonstracija Employee klase
# =========================
print("\n=== EMPLOYEE ===")

for employee in employees:
    print(f"\nIme: {employee.name}")
    print(f"Email validan: {employee.check_email()}")
    print(f"Plata pre povecanja: {employee.salary}")
    
    employee.increase_salary(10)
    
    print(f"Plata nakon povecanja: {employee.salary}")

# =========================
# Demonstracija User klase
# =========================
print("\n=== USER ===")

# Dodavanje proizvoda korisnicima
users[0].add_product(products[0])
users[0].add_product(products[1])

users[1].add_product(products[2])

users[2].add_product(products[3])
users[2].add_product(products[4])

# Prikaz podataka korisnika
for user in users:
    print(f"\nIme: {user.name}")
    print(f"Username: {user.username}")
    print(f"Email validan: {user.check_email()}")
    print(f"Ukupno potroseno: {user.total_spent()}")

    print("Kupljeni proizvodi:")
    
    for product in user.shopping_history:
        print(f"- {product.name}")