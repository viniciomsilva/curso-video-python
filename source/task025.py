# 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO
# NOME

from cli.io import printf


def run():
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
