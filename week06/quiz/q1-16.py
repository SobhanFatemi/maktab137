def sort(numbers):
    sorted_numbers = sorted(numbers, key=lambda x: (sum(int(y) for y in str(x)), x))
    return sorted_numbers

nums = [91, 23, 14, 101, 55]
result = sort(nums)
print(result)