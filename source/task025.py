# 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO
# NOME

from scripts.custom import customize


def run():
    name = input("Digite o seu nome completo: ").strip().lower()

    if "silva" in name:
        print(
            customize(
                "Parabéns! Você é um(a) Silva",
                style="bold",
                color="cyan",
            )
        )
    else:
        print(
            customize(
                "Que pena! Você NÃO faz parte dos Silvas",
                style="bold",
                color="cyan",
            )
        )
