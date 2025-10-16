class Cake:
    def __init__(self, flavor: str, size: str, price: int):
        self.flavor = flavor
        self.size = size
        self.price = price

    def describe(self):
        print(f"It's a {self.flavor} cake, It's {self.size} sized and It's {self.price} Tomans.")


chocolate_cake = Cake("Chocolate", "Medium", 600)
chocolate_cake.describe()