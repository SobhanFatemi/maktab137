from functools import reduce

products = [
    {'name': 'Laptop', 'price': 1500, 'quantity': 2},
    {'name': 'Mouse', 'price': 25, 'quantity': 10},
    {'name': 'Keyboard', 'price': 75, 'quantity': 5}
]

total_value = reduce(lambda x, product: x + (product['price'] * product['quantity']), products, 0)

print(f"Total inventory value: {total_value}")