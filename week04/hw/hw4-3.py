def repeated_more(fruits):
    cache = {}
    max_fruit = ""
    max_count = 0
    for item in fruits:
        if item in cache:
            cache[item] += 1
        else:
            cache[item] = 1
    for key, value in cache.items():
        if value > max_count:
            max_fruit = key
            max_count = value
    return max_fruit



fruits = ['orange', 'banana', 'apple', 'orange', 'apple', 'kiwi', 'apple']
print(repeated_more(fruits))