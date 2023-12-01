"""
De forma geral, o lado direito pode ter qualquer tipo de sequência (string, lista ou tupla).
Por exemplo, para dividir um endereço de email em um nome de usuário e um domínio, você poderia escrever:

>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')

O valor de retorno do split é uma lista com dois elementos; o primeiro elemento é atribuído a uname, o segundo a domain:

>>> uname
'monty'
>>> domain
'python.org'

def min_max(t):
    return min(t), max(t)
"""
