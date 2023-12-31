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

>>> s = 'pining for the fjords'
>>> t = s.split()
>>> t
['pining', 'for', 'the', 'fjords']

>>> t = ['pining', 'for', 'the', 'fjords']
>>> delimiter = ' '
>>> s = delimiter.join(t)
>>> s
'pining for the fjords'
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

# for i in cheeses:
# print(i)


cheeses = [1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
# for i in range(len(cheeses)):
#     cheeses[i] = cheeses[i] * 2
#     count += 1
#     print(f'{count}º || {cheeses}')

# print(add_all(cheeses))

cheeses = 'Olá', 'Oi', 'asda', 'b', 'o', 's'

# print(capitalize_all(cheeses))


# print(only_upper(cheeses))


"""Exercício 10.1

Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21

Exercício 10.2

Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original. Por exemplo:

>>> t = [1, 2, 3]
>>> cumsum(t)
[1, 3, 6]

Exercício 10.3

Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> middle(t)
[2, 3]

Exercício 10.4

Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne None. Por exemplo:

>>> t = [1, 2, 3, 4]
>>> chop(t)
>>> t
[2, 3]

Exercício 10.5

Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne True se a lista estiver classificada em ordem ascendente, e False se não for o caso. Por exemplo:

>>> is_sorted([1, 2, 2])
True
>>> is_sorted(['b', 'a'])
False

Exercício 10.6

Duas palavras são anagramas se você puder soletrar uma rearranjando as letras da outra. Escreva uma função chamada is_anagram que tome duas strings e retorne True se forem anagramas.
Exercício 10.7
Escreva uma função chamada has_duplicates que tome uma lista e retorne True se houver algum elemento que apareça mais de uma vez. Ela não deve modificar a lista original.

Exercício 10.8

Este exercício pertence ao assim chamado Paradoxo de aniversário, sobre o qual você pode ler em http://en.wikipedia.org/wiki/Birthday\_paradox.

Se há 23 alunos na sua sala, quais são as chances de dois deles fazerem aniversário no mesmo dia? Você pode estimar esta probabilidade gerando amostras aleatórias de 23 dias de aniversário e verificando as correspondências. Dica: você pode gerar aniversários aleatórios com a função randint no módulo random.

Se quiser, você pode baixar minha solução em http://thinkpython2.com/code/birthday.py.
Exercício 10.9

Escreva uma função que leia o arquivo words.txt e construa uma lista com um elemento por palavra. Escreva duas versões desta função, uma usando o método append e outra usando a expressão t = t + [x]. Qual leva mais tempo para ser executada? Por quê?

Solução: http://thinkpython2.com/code/wordlist.py.
Exercício 10.10

Para verificar se uma palavra está na lista de palavras, você pode usar o operador in, mas isso seria lento porque pesquisaria as palavras em ordem.

Como as palavras estão em ordem alfabética, podemos acelerar as coisas com uma busca por bisseção (também conhecida como pesquisa binária), que é semelhante ao que você faz quando procura uma palavra no dicionário. Você começa no meio e verifica se a palavra que está procurando vem antes da palavra no meio da lista. Se for o caso, procura na primeira metade da lista. Se não, procura na segunda metade.

De qualquer forma, você corta o espaço de busca restante pela metade. Se a lista de palavras tiver 113.809 palavras, o programa seguirá uns 17 passos para encontrar a palavra ou concluir que não está lá.

Escreva uma função chamada in_bisect que receba uma lista ordenada, um valor-alvo e devolva o índice do valor na lista se ele estiver lá, ou None se não estiver.

Ou você pode ler a documentação do módulo bisect e usá-lo!

Solução: http://thinkpython2.com/code/inlist.py.
Exercício 10.11

Duas palavras são um “par inverso” se uma for o contrário da outra. Escreva um programa que encontre todos os pares inversos na lista de palavras.

Solução: http://thinkpython2.com/code/reverse_pair.py.
Exercício 10.12

Duas palavras “interligam-se” quando, ao tomarmos letras alternadas de cada uma, formamos uma palavra nova. Por exemplo, “shoe” e “cold” interligam-se para formar “schooled”.

Solução: http://thinkpython2.com/code/interlock.py. Crédito: este exercício foi inspirado por um exemplo em http://puzzlers.org.

    Escreva um programa que encontre todos os pares de palavras que se interligam. Dica: não enumere todos os pares!

    Você pode encontrar palavras que sejam interligadas de três em três; isto é, cada terceira letra forma uma palavra, começando da primeira, segunda ou terceira?

"""


def nested_sum(list_):
    n = 0
    for list in list_:
        for i in list:
            n += i
    return print(n)


t = [[1, 2], [3], [4, 5, 6]]

# nested_sum(t)

# 21

#############################

list_ = [1, 2, 3, 4, 5, 6]


def cumsum(list_):
    new_list = []
    count = 0
    for i in list_:
        count += i
        new_list.append(count)

    return new_list


# print(cumsum(list_=list_))
# [1, 3, 6, 10, 15, 21]

def chop(list_):
    list_.pop(0)
    list_.pop()
    new_list = list_

    return print(new_list)


# chop(list_)
# [2, 3, 4, 5]


def is_sorted(list_):
    if list_ == sorted(list_):
        return True
    else:
        return False


opkl = [1, 2, 4, 6, 3, 1, 9]
# print(is_sorted(opkl))
# False
# print(is_sorted(list_))
# True


def is_anagram(word_1: str, word_2: str) -> bool:
    if len(word_1) != len(word_2):
        return False
    else:
        _wL1 = []
        _wL2 = []
        for i in word_1:
            _wL1.append(i.lower())
        for i in word_2:
            _wL2.append(i.lower())

        _wL1.sort()
        _wL2.sort()

        if _wL1 == _wL2:
            return True
        else:
            return False


# print(is_anagram('roma', 'amor'))
# print(is_anagram('alegria', 'Galeria'))
# print(is_anagram('Gume', 'Galeria'))
# print(is_anagram('alegria', 'Ford'))
# print(is_anagram('alegria', 'Galeria'))
# print(is_anagram('alegria', 'Ola'))
# print(is_anagram('AlErgia', 'regalia'))
