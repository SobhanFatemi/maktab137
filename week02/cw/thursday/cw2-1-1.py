def shift(word):
    new_word_list = []
    for letter in word:
        if letter == 'z':
            new_word_list.append('a')
        elif letter == 'Z':
            new_word_list.append('A')
        else:
            letter = chr(ord(letter) + 1)
            new_word_list.append(letter)
    new_word_str = ''.join(new_word_list)
    return new_word_str

print(shift("abcxyz"))