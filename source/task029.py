# 029
# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.

from utils import custom as cs


def run():
    speed = float(input("Digite a velocidade do carro (km/h): "))

    if speed <= 80:
        print(cs.colorize("Tudo bem!", color="cyan"))
    else:
        print(
            cs.colorize(
                f"Você foi multado em R$ {((speed - 80) * 7):.2f}!",
                color="lilac",
            )
        )


if __name__ == "__main__":
    run()
