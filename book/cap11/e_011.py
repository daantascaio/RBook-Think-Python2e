"""
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d


print(histogram('caio ferreira dantas lara'))

my_name_dict = histogram('Caio Ferrira Dantas Lara')
print(my_name_dict.get('a'))
print(my_name_dict.get('z'))

def print_hist(h):
    for c in h:
        print(c, h[c])

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k0
    raise LookupError()

    >>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary
"""


# # Essa função inverte  um dicionário
# def invert_dict(d):
#     inverse = dict()
#     for key in d:
#         val = d[key]
#         if val not in inverse:
#             inverse[val] = [key]
#         else:
#             inverse[val].append(key)
#     return inverse
from pathlib import Path
from pprint import pprint

PATH_WORDS_FILE = Path(__file__).parent / 'words.txt'
words = {}

with open(PATH_WORDS_FILE, 'r') as file:
    for line in file:
        word_line = line.split()
        for word in word_line:
            words[word] = ''
    print(words)

if 'Caio' in words:
    print('Caio')

pprint(words)
