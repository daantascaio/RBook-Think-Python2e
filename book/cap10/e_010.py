"""
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']

['spam', 2.0, 5, [10, 20]]

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)
['Cheddar', 'Edam', 'Gouda'] [42, 123] []

cheeses[0]
'Cheddar'

numbers = [42, 123]
numbers[1] = 5
numbers
[42, 5]

cheeses = ['Cheddar', 'Edam', 'Gouda']
'Edam' in cheeses
True
'Brie' in cheeses
False

for cheeses in cheeses
    print(cheeses)



t = ['a', 'b', 'c']
t.append('d')
t
['a', 'b', 'c', 'd']

>>> t1 = ['a', 'b', 'c']
>>> t2 = ['d', 'e']
>>> t1.extend(t2)
>>> t1
['a', 'b', 'c', 'd', 'e']


>>> t = ['d', 'c', 'e', 'b', 'a']
>>> t.sort()
>>> t
['a', 'b', 'c', 'd', 'e']

>>> t = [1, 2, 3]
>>> sum(t)
6


>>> t = ['a', 'b', 'c']
>>> x = t.pop(1)
>>> t
['a', 'c']
>>> x
'b'

>>> t = ['a', 'b', 'c']
>>> del t[1]
>>> t
['a', 'c']

>>> t = ['a', 'b', 'c']
>>> t.remove('b')
>>> t
['a', 'c']


>>> s = 'spam'
>>> t = list(s)
>>> t
['s', 'p', 'a', 'm']
"""


def add_all(list):
    total = 0
    for x in list:
        total += x
    return total


def capitalize_all(list):
    res = []
    for s in list:
        res.append(s.capitalize())
    return res


# def only_upper(t):
#     res = []
#     for s in t:
#         if s.isupper():
#             res.append(s)
#     return res


cheeses = []

cheeses += 'Olá', 2, 2.5, 'Oi', 'AIUSHD'

for i in cheeses:
    print(i)


cheeses = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
for i in range(len(cheeses)):
    cheeses[i] = cheeses[i] * 2
    count += 1
    print(f'{count}º || {cheeses}')

print(add_all(cheeses))

cheeses = 'Olá', 'Oi', 'asda', 'b', 'o', 's'

print(capitalize_all(cheeses))


# print(only_upper(cheeses))
