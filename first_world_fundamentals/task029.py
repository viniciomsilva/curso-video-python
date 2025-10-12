# 029
# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.

from custom import clear
from custom import customize

if __name__ == "__main__":
    speed = float(input("DIGITE A VELOCIDADE DO CARRO (KM/H): "))

    if speed <= 80:
        print(
            "{}TUDO BEM!".format(
                customize(style="bold", color="cyan"),
            )
        )
    else:
        print(
            "VOCÊ FOI MULTADO EM {}R$ {:.2f}{}!".format(
                customize(style="bold", color="lilac"),
                ((speed - 80) * 7),
                clear(),
            )
        )
