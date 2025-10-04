numbers: list = [1, 2, 3, 4]

print(numbers)

numbers[1] = 32

print(numbers)

numbers.append(89)

print(numbers)

numbers.remove(3)

if 3 in numbers:
    print("You win the lottary!")
else:
    print("You lost!")

if 22 not in numbers:
    print("You have cancer!")
else:
    print("You do not have cancer!")

numbers.append(4)

print(numbers)

index: int = numbers.index(4)

print(index)

number_count: int = numbers.count(4)

print(number_count)

del numbers[0]

print(numbers)

result: int = sum(numbers)

print(result)

max_item: int = max(numbers)

print(max_item)

sorted_list: list = sorted(numbers)

print(sorted_list)

sorted_list_desk: list = sorted(numbers, reverse=True)

print(sorted_list_desk)

numbers.insert(0, 201)

print(numbers)

fruits: list = ["orange", "banana", "apple"]
fruits.sort()
print(fruits)
print(len(fruits))
print(len(fruits[2]))
