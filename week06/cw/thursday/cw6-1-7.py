class ShoppingCart:
    def __init__(self, items: list):
        self.__items = items

    def add_item(self, item):
        if item in self.__items:
            print("It's already in your cart!")
        else:
            self.__items.append(item)

    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
        else:
            print("It's not in the cart!")
    
    def show_items(self):
        print(self.__items)
        # for i, item in enumerate(self.__items):
        #     print(f"#{i+1}: {item}")
    

cart = ShoppingCart([])
cart._ShoppingCart__items.append("Orange")
cart.add_item("Banana")
cart.show_items()
cart.add_item("Banana")
cart.add_item("Apple")
cart.show_items()
cart.remove_item("Apple")
cart.show_items()