# 001
# FAÇA UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE UMA MENSAGEM
# DE BOAS VINDAS

from cli.io import inputf
from cli.io import printf


def run():
    name = inputf("Qual é o seu nome? ", style="bold")

    printf(
        "Olá, {}, seja bem-vindo(a) ao Mundo do 🐍 Python!".format(
            name.title(),
        ),
        start="\n",
        style="bold",
    )
