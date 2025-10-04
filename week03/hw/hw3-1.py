import itertools
import copy

words = []
while True:
    user_choice = input("To type sentence type 'sentence' and for words type 'words': ")
    if user_choice == "sentence":
        while True:
            user_input = input("Please enter your sentence: ")
            words = user_input.split()
            if len(words) < 4:
                print("It has to be 4 or more words.")
                continue
            else:
                break
        break
    elif user_choice == "words":
        while True:
            try:
                words_count = int(input("Type how many words: "))
                if words_count < 4:
                    print("It has to be 4 or more words.")
                    continue
                else:
                    for count in range(1, words_count + 1):
                        user_input = input(f"Type word #{count}: ")
                        words.append(user_input)
                    break
            except ValueError:
                print("Invalid input!")
                continue
        break
    else:
        print("Wrong input!")
        continue

def combo_generator(words, i):
    for combo in itertools.combinations(words, i):
        yield list(combo)

combos = []

for i in range(2, 5):
    combos.append(list(combo_generator(words, i)))

combo_2 = combos[0]
combo_3 = combos[1]
combo_4 = combos[2]

print(combos)

# shallow_copy_combos = copy.copy(combo_4)
# shallow_copy_combos[0][0] = "maktab137" 
# print(f"Original after shallow copy: {combo_4}")
# print(f"Shallow copy: {shallow_copy_combos}")

# deep_copy_combos = copy.deepcopy(combo_3)
# deep_copy_combos[0][0] = "maktab137"
# print(f"Original after deep copy: {combo_3}")
# print(f"Deep copy: {deep_copy_combos}")