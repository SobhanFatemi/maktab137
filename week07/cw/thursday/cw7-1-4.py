class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price

    def __add__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Value must be a Product!")
        if self == other:
            return Product(self.name, self.price, self.quantity + other.quantity)
        else:
            return Product(f"{self.name} & {other.name}", self.price + other.price, self.quantity + other.quantity)

    def __str__(self):
        return f"{self.name}: ${self.price} ({self.quantity} left)"

    def __del__(self):
        print(f"'{self.name}' was deleted from memory!")


p1 = Product("Apple", 1.5, 30)
p2 = Product("Apple", 1.5, 20)
p3 = Product("Banana", 1.0, 15)

print(p1)  
print(p2)  
print(p3)  

p4 = p1 + p2
print(p4) 

p5 = p1 + p3
print(p5)  
