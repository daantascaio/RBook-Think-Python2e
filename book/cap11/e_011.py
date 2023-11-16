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
            return k
    raise LookupError()

    >>> raise LookupError('value does not appear in the dictionary')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
LookupError: value does not appear in the dictionary
"""
