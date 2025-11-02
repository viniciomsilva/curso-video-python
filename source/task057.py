# 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' e
# 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

from cli.io import printf


def run():
    while True:
        sex = input("Digite o sexo [M/F]: ").strip()[0]

        if sex in "MmFf":
            printf(
                "Muito bem. Obrigado!",
                style="bold",
                color="cyan",
            )
            break
        else:
            printf(
                "Por favor, digite um valor válido!",
                style="bold",
                color="magenta",
            )
