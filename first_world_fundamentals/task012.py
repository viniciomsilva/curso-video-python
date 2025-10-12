# 012
# FAÇA UM PROGRAMA QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE-O COM 5% DE DESCONTO

from custom import customize

if __name__ == "__main__":
    price = float(input("DIGITE O VALOR DO PRODUTO...........: R$ "))
    discount = float(input("DIGITE A PORCENTAGEM DE DESCONTO (%):    "))

    print(
        "\nVALOR TOTAL.........................: {}R$ {:.2f}".format(
            customize(style="bold", color="lilac"),
            (price * (1 - discount / 100)),
        )
    )
