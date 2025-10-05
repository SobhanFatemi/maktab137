def nested_sum(my_list):
    result = 0
    for item in my_list:
        if type(item) == list:
            result += nested_sum(item)
        else:
            result += item
    return result

print(nested_sum([1, [2,3], [4, [5]]]))