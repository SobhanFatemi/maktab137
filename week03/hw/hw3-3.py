def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    smaller = []
    bigger = []
    for i in range(1, len(numbers)):
        if numbers[i] > pivot:
            bigger.append(numbers[i])
        else:
            smaller.append(numbers[i])
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]
    
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)
    
    merged = []
    i = j = 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] <= sorted_right[j]:
            merged.append(sorted_left[i])
            i += 1
        else:
            merged.append(sorted_right[j])
            j += 1
    
    while i < len(sorted_left):
        merged.append(sorted_left[i])
        i += 1
    while j < len(sorted_right):
        merged.append(sorted_right[j])
        j += 1
    
    return merged


numbers_1 = [19, 1, 8, 13, 3, 2]
bubble_sort((numbers_1))
print(numbers_1)

numbers_2 = [32, 1, 31, 44, 5645, 2, 3, 41, 4]
print(quick_sort(numbers_2))

numbers_3 = [4124, 21, 214 , 43, 14, 2]
print(merge_sort(numbers_3))