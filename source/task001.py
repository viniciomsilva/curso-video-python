# 001
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE UMA MENSAGEM
# DE BOAS VINDAS

from scripts.custom import customize


def run():
    name = input("Qual é o seu nome? ")

    print(
        customize(
            "\nOlá, {}, seja bem-vindo(a) ao Mundo do 🐍 Python!".format(
                name.title(),
            ),
            style="bold",
        )
    )
