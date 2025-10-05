def repeated_more(my_list):
    cache = {}
    max_fruit = ""
    max_count = 0
    for item in my_list:
        if item in cache:
            cache[item] += 1
        else:
            cache[item] = 1
    for key, value in cache.items():
        if value > max_count:
            max_fruit = key
            max_count = value
    return max_fruit



my_list = ['orange', 'banana', 'apple', 'orange', 'apple', 'kiwi', 'apple']
print(repeated_more(my_list))