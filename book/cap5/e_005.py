"""O último teorema de Fermat diz que não existem números inteiros a, b e c tais que a**n + b**n == c**n para quaisquer valores de n maiores que 2.

    Escreva uma função chamada check_fermat que receba quatro parâmetros - a, b, c e n - e verifique se o teorema de Fermat se mantém. Se n for maior que 2 e a**n + b**n == c**n o programa deve imprimir, “Holy smokes, Fermat was wrong!” Senão o programa deve exibir “No, that doesn't work.”

    Escreva uma função que peça ao usuário para digitar valores para a, b, c e n, os converta em números inteiros e use check_fermat para verificar se violam o teorema de Fermat.
"""


def check_format(a: int, b: int, c: int, n: int):

    if n > 2 and a**n + b**n == c**n:
        return print("Holy smokes, Fermat was wrong!")

    print("No, that doesn't work.")


check_format(10, 2, 5, 4)
