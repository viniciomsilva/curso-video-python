# 001
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem
# de boas vindas.

from cli.io import inputf
from cli.io import printf


if __name__ == "__main__":
    name = inputf("Qual é o seu nome? ", style="bold")

    printf(
        "Olá, {}, seja bem-vindo(a) ao Mundo do 🐍 Python!".format(
            name.title(),
        ),
        start="\n",
        style="bold",
    )
