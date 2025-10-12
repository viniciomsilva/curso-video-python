# 001
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE UMA MENSAGEM
# DE BOAS VINDAS

from custom import clear
from custom import customize

if __name__ == "__main__":
    name = input("QUAL É O SEU NOME? ")

    print(
        "OLÁ, {}, SEJA BEM-VINDO(A) AO 1º MUNDO DE {}PYT{}{}HON{}!".format(
            name.upper(),
            customize(color="blue"),
            clear(),
            customize(color="yellow"),
            clear(),
        )
    )
