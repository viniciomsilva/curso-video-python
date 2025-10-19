# 015
# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
# ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A
# PAGAR, SABENDO QUE O CARRO CUSTA R$ 60,00 POR DIA E R$ 0,15 POR KM RODADO

from scripts.custom import customize


def calc_rent(qnt_day, qnt_km):
    return qnt_day * 60 + qnt_km * 0.15


def run():
    qnt_days = int(input("Digite a quantidade de dias: "))
    qnt_km = float(input("Digite quantos quilômetros foram rodados: "))

    print(
        "\nValor total: {}".format(
            customize(
                "R$ {:.2f}".format((calc_rent(qnt_days, qnt_km))),
                style="bold",
                color="cyan",
            ),
        )
    )
