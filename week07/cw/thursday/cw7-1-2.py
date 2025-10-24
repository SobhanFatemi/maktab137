class Car:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def __str__(self):
        return f"'{self.model}': '{self.brand}', '${self.price}'"
    
    def __eq__(self, other):
        if not isinstance(other, Car):
            raise ValueError("Value must be a car!")
        return self.model == other.model and self.brand == other.brand
    
    def __add__(self, other):
        if not isinstance(other, Car):
            raise ValueError("Value must be a Car!")
        if self == other:
            return Car(self.model, self.brand, self.price + other.price)
        return Car(f"{self.model} & {other.model}", f"{self.brand} & {other.brand}", self.price + other.price)
    
    def __del__(self):
        return f"'{self.brand}' was deleted from memory!"
    
car1 = Car("Model S", "Tesla", 90000)
car2 = Car("Model S", "Tesla", 95000)
car3 = Car("Mustang", "Ford", 55000)

print(car1)  
print(car2)  
print(car3)  


print(car1 == car2)  
print(car1 == car3)  


car4 = car1 + car2
print(car4)  

car5 = car1 + car3
print(car5) 