# 001
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE UMA MENSAGEM
# DE BOAS VINDAS

from scripts.custom import customize as cs


def run():
    name = input(cs("Qual é o seu nome? ", "bold"))

    print(
        cs(
            "Olá, {}, seja bem-vindo(a) ao Mundo do Python!".format(
                name.title(),
            ),
            "bold",
        )
    )
