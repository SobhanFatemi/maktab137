from string import ascii_lowercase, ascii_uppercase, digits, punctuation

def is_valid(passwd):
    if len(passwd) < 8:
        return False
    has_lower = has_upper = has_num = has_punc = False
    for char in passwd:
        if char in ascii_lowercase:
            has_lower = True
        elif char in ascii_uppercase:
            has_upper = True
        elif char in digits:
            has_num = True
        elif char in punctuation:
            has_punc = True
    return has_lower and has_upper and has_num and has_punc

while True:
    passwd = input()
    if not is_valid(passwd):
        print('invalid password')
    else:
        print('valid password')
        break