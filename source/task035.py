# 035
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS SEGMENTOS DE RETA E DIGA
# AO USUÁRIO SE ELES PODEM OU NÃO FORMAR UM TRIÂNGULO.

# REGRA DA DESIGUALDADE TRIANGULAR
#   A SOMA DE DOIS QUAISQUER SEGMENTOS DEVE SER MAIOR QUE O TERCEIRO

from scripts.custom import customize


def form_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def run():
    a = float(input("Digite o valor do 1º segmento: "))
    b = float(input("Digite o valor do 2º segmento: "))
    c = float(input("Digite o valor do 3º segmento: "))

    print(
        customize(
            "Podem formar um triângulo",
            style="bold",
            color="cyan",
        )
        if form_triangle(a, b, c)
        else customize(
            "Não podem formar um triângulo",
            style="bold",
            color="magenta",
        )
    )
