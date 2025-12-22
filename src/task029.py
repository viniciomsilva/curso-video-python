# 029
# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.

from cli.io import printf


def __calc(speed):
    return (speed - 80) * 7


def run():
    speed = float(input("Digite a velocidade do carro (km/h): "))

    if speed <= 80:
        printf(
            "Tudo bem!",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "Você foi multado em R$ {:.2f}!".format(__calc(speed)),
            style="bold",
            color="magenta",
        )


if __name__ == "__main__":
    run()
