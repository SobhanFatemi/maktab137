def max_min(my_list):
    max_item = max(my_list)
    min_item = min(my_list)
    return max_item, min_item

my_list = [3, 4, 28 , 8, 1]

result = max_min(my_list)

print(f"Biggest number was: {result[0]}\nSmallest number was: {result[1]}")