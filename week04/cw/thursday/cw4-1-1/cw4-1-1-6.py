products = [
    {'name': 'A', 'price': 150, 'rating': 4.5},
    {'name': 'B', 'price': 200, 'rating': 4.2},
    {'name': 'C', 'price': 120, 'rating': 4.5},
    {'name': 'D', 'price': 250, 'rating': 4.8},
    {'name': 'E', 'price': 180, 'rating': 4.2}
]

sorted_products = sorted(products, key=lambda x: x['rating'], reverse=True)

i = 0
while i < len(products) - 1:
    if sorted_products[i]['rating'] == sorted_products[i + 1]['rating'] and sorted_products[i]['price'] > sorted_products[i + 1]['price']:
            sorted_products[i], sorted_products[i + 1] = sorted_products[i + 1], sorted_products[i]
    i += 1

for p in sorted_products:
    print(p)
