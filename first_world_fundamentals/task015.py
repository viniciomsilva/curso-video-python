# 015
# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO
# ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A
# PAGAR, SABENDO QUE O CARRO CUSTA R$ 60,00 POR DIA E R$ 0,15 POR KM RODADO

from custom import customize


if __name__ == "__main__":
    qnt_days = int(input("DIGITE A QUANTIDADE DE DIAS ALUGADOS......: "))
    qnt_km = float(input("DIGITE A QUANTIDADE DE QUILÔMETROS RODADOS: "))

    print(
        "VALOR TOTAL A PAGAR.......................: {}R$ {:.2f}".format(
            customize(style="bold", color="cyan"),
            (qnt_days * 60 + qnt_km * 0.15),
        )
    )
