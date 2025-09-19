import re
from collections import Counter

def count_words(text):
    words = re.findall(r'\w+', text.lower())
    return len(words)

def term_frequency(text):
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def find_palindromes(text):
    words = set(re.findall(r'\w+', text.lower()))
    return [w for w in words if len(w) > 1 and w == w[::-1]]
