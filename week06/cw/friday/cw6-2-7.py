class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price}$"

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __str__(self):
        return '\n'.join([item.name for item in self.items])
    
    def __len__(self):
        return len(self.items)
    
    def __contains__(self, item):
        if item in self.items:
            return True
        return False
    
    def __add__(self, other_cart):
        new_cart = ShoppingCart([])
        new_cart.items = self.items + other_cart.items
        return new_cart

    def add_item(self, *items):
        for item in items:
            self.items.append(item)

    def remove_item(self, *items):
        for item in items:
            self.items.remove(item)

    def total_price(self):
        total = 0
        for item in self.items:
            total += item.price

        return total

cart1 = ShoppingCart([])
ice_cream = Item("Ice cream", 3)
chocolate_bar = Item("Chocolate Bar", 2)
sandwich = Item("Sandwich", 5)
apple = Item("Apple", 1)
bottle_water = Item("Bottle of Water", 2)
cart1.add_item(ice_cream, chocolate_bar, sandwich, apple, bottle_water)

cart2 = ShoppingCart([])
chips = Item("Chips", 3)
coffee = Item("Coffee", 4)
donut = Item("Donut", 2)
pizza_slice = Item("Pizza Slice", 4)
salad = Item("Salad", 6)
cart2.add_item(chips, coffee, donut, pizza_slice, salad)
cart2.remove_item(chips)

print(chips)

print(cart2)

print(len(cart2))

print(apple in cart1)
print(apple in cart2)

combined_cart = cart1  + cart2

print(combined_cart)

print(cart1.total_price())