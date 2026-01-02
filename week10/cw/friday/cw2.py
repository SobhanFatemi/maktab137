import argparse
import os
import re as regex
from collections import Counter

def print_hello():
    print("Hello")

def reverse_string(string):
    print(string[::-1])

def count_word(filepath):
    words_count = {}
    
    if not os.path.isfile(filepath):
        raise FileNotFoundError
    
    with open(filepath, 'r') as file:
        text = file.read().lower()

    words = text.split()

    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    return words_count
    
    

