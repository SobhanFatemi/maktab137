class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def sell(self, amount):
        if self.quantity < amount:
            print(f"Not enough {self.name}!")
        else:
            self.quantity -= amount

    def restock(self, amount):
        self.quantity += amount

    def desplay_info(self):
        print(f"Name: {self.name}\nPrice: {self.price}\n{self.name} left: {self.quantity}")


class Inventory:
    def __init__(self, products=[]):
        self.products = products

    def add_product(self, *args):
        for arg in args:
            if arg in self.products:
                print(f"{arg.name} was already added!")
            else:
                self.products.append(arg)
                print(f"{arg.name} was added!")

    def update_product(self, product, price):
        if product.price != price:
            product.price = price
            print(f"Price of {product.name} was updated.")
        else:
            print(f"Price of {product.name} is already {price}!")

    def delete_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"{product.name} was removed.")
        else:
            print(f"{product.name} was not found.")

    def read_inventory(self):
        for product in self.products:
            product.desplay_info()
        

biscuit = Product("Biscuit", 5, 200)
biscuit.sell(120)
biscuit.restock(100)

ice_cream = Product("Ice Cream", 20, 100)
ice_cream.sell(20)
ice_cream.restock(50)

energy_drink = Product("Energy Drink", 50, 50)
ice_cream.sell(10)
ice_cream.restock(50)

soda = Product("Soda", 30, 100)


inventory = Inventory()
inventory.add_product(ice_cream, biscuit, energy_drink)
inventory.update_product(energy_drink, 50)
inventory.update_product(biscuit, 7)
inventory.delete_product(soda)
inventory.delete_product(ice_cream)
inventory.read_inventory()