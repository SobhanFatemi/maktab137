import copy

def cache_decorator(func):
    cache ={}
    def wrapper(sentence):
        if sentence in cache:
            print("You entered cache!")
            return copy.deepcopy(cache[sentence])
        result = func(sentence)
        cache[sentence] = result
        return copy.deepcopy(result)
    return wrapper

@cache_decorator
def word_count(sentence):

    filtered_input = filter(lambda letter: 97 <= ord(letter) <= 122 or letter == ' ', sentence)

    filtered_input_str = ''.join(filtered_input)

    words = filtered_input_str.split()

    sobhan_counter = 0
    fatemi_counter = 0
    for word in words:
        if word == "sobhan":
            sobhan_counter += 1
        elif word == "fatemi":
            fatemi_counter += 1
    return [sobhan_counter, fatemi_counter]

user_input = "Sobhan, sobhan! FATEMI?? . sobhan FAtemi".lower()
word_count(user_input)[0] += 1
print(word_count(user_input))
word_count(user_input)[0] += 1
print(word_count(user_input))