def multiplier(number, choice):

    def double(n):
        return n * 2

    def triple(n):
        return n * 3

    if choice == 'double':
        return double(number)
    elif choice == 'triple':
        return triple(number)
    else:
        return "Invalid choice! Use 'double' or 'triple'."

print(multiplier(5, 'double')) 
print(multiplier(5, 'triple')) 