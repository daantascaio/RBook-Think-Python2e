import math
import turtle


"""bob = turtle.Turtle()
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

print(bob)


for i in range(4):
    print('Hello!')

for i in range(4):
    bob.fd(100)
    bob.lt(90)


turtle.mainloop()
"""

"""
    1-Escreva uma função chamada square que receba um parâmetro chamado t, que é um turtle. Ela deve usar o turtle para desenhar um quadrado.

        Escreva uma chamada de função que passe bob como um argumento para o square e então execute o programa novamente.

    2-Acrescente outro parâmetro, chamado length, ao square. Altere o corpo para que o comprimento dos lados seja length e então altere a chamada da função para fornecer um segundo argumento. Execute o programa novamente. Teste o seu programa com uma variedade de valores para length.

    3-Faça uma cópia do square e mude o nome para polygon. Acrescente outro parâmetro chamado n e altere o corpo para que desenhe um polígono regular de n lados.

        Dica: os ângulos exteriores de um polígono regular de n lados são 360/n graus.

    4-Escreva uma função chamada circle que use o turtle, t e um raio r como parâmetros e desenhe um círculo aproximado ao chamar polygon com um comprimento e número de lados adequados. Teste a sua função com uma série de valores de r.

        Dica: descubra a circunferência do círculo e certifique-se de que length * n = circumference.

    5-Faça uma versão mais geral do circle chamada arc, que receba um parâmetro adicional de angle, para determinar qual fração do círculo deve ser desenhada. angle está em unidades de graus, então quando angle=360, o arc deve desenhar um círculo completo.

"""


bob = turtle.Turtle()


def square(t, length: int):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polyline(t, n, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    arc(t, r, 360)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)


draw(bob, 5, 20)
