# 035
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS SEGMENTOS DE RETA E DIGA
# AO USUÁRIO SE ELES PODEM OU NÃO FORMAR UM TRIÂNGULO.

# REGRA DA DESIGUALDADE TRIANGULAR
#   A SOMA DE DOIS QUAISQUER SEGMENTOS DEVE SER MAIOR QUE O TERCEIRO

# 042
# REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRAR QUE
# TIPO DE TRIÂNGULO SERÁ FORMADO.
# 	- EQUILÁTERO:	TODOS OS LADOS IGUAIS
# 	- ISÓSCELES:	DOIS LADOS IGUAIS
# 	- ESCALENO:     TODOS OS LADOS DIFERENTES

from cli.io import printf
from cli.wait import wait


def __is_triangle(a, b, c):
    # Triangular inequality rule:
    # The sum of any two segments must be greater than the third.
    return a + b > c and a + c > b and b + c > a


def __form_triangle(segments):
    response = {
        "msg": "👎 Não formam um triângulo.",
        "color": "magenta",
    }

    if __is_triangle(segments[0], segments[1], segments[2]):
        response["color"] = "cyan"

        match len(set(segments)):  # set does not allow duplicated data
            case 1:
                response["msg"] = "👍 Formam um triângulo equilátero."
            case 2:
                response["msg"] = "👍 Formam um triângulo isósceles."
            case 3:
                response["msg"] = "👍 Formam um triângulo escaleno."

    return response


def run():
    segments = []

    for i in range(3):
        seg = float(input("Valor do {}º segmento: ".format(i + 1)))
        segments.append(seg)

    wait("Analisando...")
    response = __form_triangle(segments)

    printf(
        response["msg"],
        style="bold",
        color=response["color"],
    )
