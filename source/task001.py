# 001
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE UMA MENSAGEM
# DE BOAS VINDAS

from utils import custom as cs


def run():
    name = input("Qual é o seu nome? ")

    print(
        "Olá, {}, seja bem-vindo(a) ao Mundo de {}Pyt{}{}hon{}!".format(
            name.title(),
            cs.customize(color="blue"),
            cs.clean(),
            cs.customize(color="yellow"),
            cs.clean(),
        )
    )


if __name__ == "__main__":
    run()
