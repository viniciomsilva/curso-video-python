# 029
# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.

from scripts.custom import customize


def calc_fine(speed):
    return (speed - 80) * 7


def run():
    speed = float(input("Digite a velocidade do carro (km/h): "))

    if speed <= 80:
        print(
            customize(
                "Tudo bem!",
                style="bold",
                color="cyan",
            )
        )
    else:
        print(
            customize(
                "Você foi multado em R$ {:.2f}!".format(calc_fine(speed)),
                style="bold",
                color="magenta",
            )
        )
