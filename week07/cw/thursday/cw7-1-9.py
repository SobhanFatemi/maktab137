class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def __len__(self):
        return len(self.products)
    
    def __add__(self, other):
        if not isinstance(other, Cart):
            raise ValueError("Value must be a Cart!")
        return Cart(self.products + other.products)
    
    def __str__(self):
        total = sum(product.price for product in self.products)
        products = '\n'.join(f"{i+1}. {product.name}" for i, product in enumerate(self.products))
        return f"Products in cart:\n{products}\nTotal: ${total}"
    
    def __del__(self):
        print("Cart deleted from memory!")


p1 = Product("Laptop", 1200)
p2 = Product("Mouse", 25)
p3 = Product("Keyboard", 75)

cart1 = Cart([p1, p2])
cart2 = Cart([p3])

cart3 = cart1 + cart2

print(cart3)