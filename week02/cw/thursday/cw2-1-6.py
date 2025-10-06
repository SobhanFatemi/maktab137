def check_palindrome(word):
    if word == word[::-1]:
        return "YES!"
    else:
        return "NO!"

print(check_palindrome("madam"))

print(check_palindrome("abc"))
