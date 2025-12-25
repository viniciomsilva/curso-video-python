# 025
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no
# nome.

from cli.io import printf


if __name__ == "__main__":
    name = input("Digite o seu nome completo: ").strip().lower()

    if "silva" in name:
        printf(
            "Parabéns! Você é um(a) Silva",
            start="\n",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "Que pena! Você NÃO faz parte dos Silvas",
            start="\n",
            style="bold",
            color="cyan",
        )
