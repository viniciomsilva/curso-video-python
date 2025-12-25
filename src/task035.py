# 035
# Desenvolva um programa que leia o comprimento de três segmentos de reta e diga
# ao usuário se eles podem ou não formar um triângulo.

# Regra da desigualdade triangular:
#   - A soma de dois quaisquer segmentos deve ser maior que o terceiro.

# 042
# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
#   - Equilátero (todos os lados iguais);
#   - Isósceles (dois lados iguais);
#   - Escaleno (todos os lados diferentes).

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import wait


def __is_triangle(a: float, b: float, c: float):
    # Triangular inequality rule:
    # The sum of any two segments must be greater than the third.
    return a + b > c and a + c > b and b + c > a


def __form_triangle(segments: list[float]) -> dict[str, str]:
    response = {
        "msg": "👎 Não formam um triângulo.",
        "color": "magenta",
    }

    if __is_triangle(segments[0], segments[1], segments[2]):
        response["color"] = "cyan"

        match set(segments).__len__():  # set does not allow duplicated data
            case 1:
                response["msg"] = "👍 Formam um triângulo equilátero."
            case 2:
                response["msg"] = "👍 Formam um triângulo isósceles."
            case 3:
                response["msg"] = "👍 Formam um triângulo escaleno."
            case _:
                ...

    return response


if __name__ == "__main__":
    segments: list[float] = []

    for i in range(3):
        seg = inputf_flo(f"Valor do {(i + 1)}º segmento: ")
        segments.append(seg)

    wait("Analisando...")
    response = __form_triangle(segments)

    printf(
        response["msg"],
        style="bold",
        color=response["color"],
    )
