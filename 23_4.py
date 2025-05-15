# create a class about laptop with 10 instances
class Laptop:
    def __init__(self, brand, model, price, ram, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
        self.storage = storage
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price: ₹", self.price)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
l1 = Laptop("Dell", "Inspiron 15", 50000, "8GB", "512GB SSD")
l2 = Laptop("HP", "Pavilion x360", 60000, "8GB", "1TB HDD")
l3 = Laptop("Lenovo", "IdeaPad Slim 3", 45000, "8GB", "256GB SSD")
l4 = Laptop("Asus", "Vivobook 14", 47000, "16GB", "512GB SSD")
l5 = Laptop("Acer", "Aspire 5", 40000, "8GB", "1TB HDD")
l6 = Laptop("Apple", "MacBook Air", 95000, "8GB", "256GB SSD")
l7 = Laptop("MSI", "Modern 14", 55000, "16GB", "512GB SSD")
l8 = Laptop("Samsung", "Galaxy Book", 52000, "8GB", "256GB SSD")
l9 = Laptop("Realme", "Book Slim", 48000, "8GB", "512GB SSD")
l10 = Laptop("Microsoft", "Surface Laptop Go", 65000, "8GB", "128GB SSD")
l1.display()
l2.display()
l3.display()
l4.display()
l5.display()
l6.display()
l7.display()
l8.display()
l9.display()
l10.display()

#output:-
# Brand: Dell
# Model: Inspiron 15
# Price: ₹ 50000
# RAM: 8GB
# Storage: 512GB SSD
# Brand: HP
# Model: Pavilion x360
# Price: ₹ 60000
# RAM: 8GB
# Storage: 1TB HDD
# Brand: Lenovo
# Model: IdeaPad Slim 3
# Price: ₹ 45000
# RAM: 8GB
# Storage: 256GB SSD
# Brand: Asus
# Model: Vivobook 14
# Price: ₹ 47000
# RAM: 16GB
# Storage: 512GB SSD
# Brand: Acer
# Model: Aspire 5
# Price: ₹ 40000
# RAM: 8GB
# Storage: 1TB HDD
# Brand: Apple
# Model: MacBook Air
# Price: ₹ 95000
# RAM: 8GB
# Storage: 256GB SSD
# Brand: MSI
# Model: Modern 14
# Price: ₹ 55000
# RAM: 16GB
# Storage: 512GB SSD
# Brand: Samsung
# Model: Galaxy Book
# Price: ₹ 52000
# RAM: 8GB
# Storage: 256GB SSD
# Brand: Realme
# Model: Book Slim
# Price: ₹ 48000
# RAM: 8GB
# Storage: 512GB SSD
# Brand: Microsoft
# Model: Surface Laptop Go
# Price: ₹ 65000
# RAM: 8GB
# Storage: 128GB SSD
