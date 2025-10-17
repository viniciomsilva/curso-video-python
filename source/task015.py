# 015
# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
# ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A
# PAGAR, SABENDO QUE O CARRO CUSTA R$ 60,00 POR DIA E R$ 0,15 POR KM RODADO

from utils import custom as cs


def calc(qnt_day, qnt_km):
    return qnt_day * 60 + qnt_km * 0.15


def run():
    qnt_days = int(input("Digite a quantidade de dias: "))
    qnt_km = float(input("Digite quantos quilômetros foram rodados: "))

    print(
        "\nValor total: {}".format(
            cs.colorize(f"R$ {(calc(qnt_days, qnt_km)):.2f}", color="cyan"),
        )
    )


if __name__ == "__main__":
    run()
