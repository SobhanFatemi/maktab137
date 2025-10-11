def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        print("Index is out of range!")


my_list = [1, 2, 3]
print_list_element(my_list, 3)