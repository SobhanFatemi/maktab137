class PositiveInteger:
    def __init__(self):
        self.storage = {}

    def __get__(self, instance, owner):
        return self.storage.get(instance)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if value <= 0:
            raise ValueError("Value must be positive")
        self.storage[instance] = value

class Product:
    price = PositiveInteger()
    quantity = PositiveInteger()

p = Product()
p.price = 50

print(p.price)      
p.price = -10