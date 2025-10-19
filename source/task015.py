# 015
# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
# ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A
# PAGAR, SABENDO QUE O CARRO CUSTA R$ 60,00 POR DIA E R$ 0,15 POR KM RODADO

from cli.io import printf


def __calc(days, kms):
    return days * 60 + kms * 0.15


def run():
    days = int(input("Digite a quantidade de dias: "))
    kms = float(input("Digite quantos quilômetros foram rodados: "))

    printf(
        "Valor total: R$ {:.2f}".format(__calc(days, kms)),
        start="\n",
        style="bold",
        color="cyan",
    )
