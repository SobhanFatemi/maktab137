num_1 = 10
num_2 = 2

result_1: bool = num_1 == num_2
result_2: bool = num_1 > num_2
result_3: bool = num_1 < num_2
result_4: bool = num_1 >= num_2
result_5: bool = num_1 <= num_2
result_6: bool = num_1 != num_2

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)

# num_1 = num_1 + num_2
num_1 += num_2
print(num_1)

# num_1 = num_1 - num_2
num_2 -= num_1
print(num_2)

# num_1 = num_1 * num_2
num_2 *= num_1

# num_1 = num_1 ** num_2
num_2 **= num_1

# num_1 = num_1 / num_2
num_2 /= num_1

# num_1 = num_1 // num_2
num_2 //= num_1

# num_1 = num_1 % num_2
num_2 %= num_1

# and, or, not
# 0  None '' "" false
num_3: any = 0
num_4: int = 3

result_7: int = num_3 and num_4
print(result_7)

result_8: int = num_3 or num_4
print(result_8)

result_9: bool = not num_4
print(result_9)

result_10: bool = not num_3
print(result_10)
