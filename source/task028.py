# 028
# ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" NUM NÚMERO INTEIRO ENTRE 0 E 5 E
# PEÇA AO USUÁRIO PARA ADIVINHAR O NÚMERO ESCOLHIDO.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU NÃO.

from time import sleep
from random import randint

from cli.io import inputf
from cli.io import printf
from cli.wait import wait


def run():
    win = False
    attempt = 1
    draw_num = randint(1, 10)

    printf(
        "Entre 0 e 10, em qual número estou pensando?",
        style="bold",
        color="cyan",
    )
    printf(
        "Você tem 4 tentativas. Boa sorte!",
        style="bold",
        color="yellow",
    )

    while not win and attempt <= 4:
        num = int(
            inputf(
                "Digite sua {}º tentativa: ".format(attempt),
                start="\n",
            )
        )

        wait("Processando...", end="\n")

        if num == draw_num:
            printf(
                "🥳 Parabéns! Você ganhou!",
                style="bold",
                color="cyan",
            )
            win = True
        elif not win:
            printf(
                "HA HA!!! Tente novamente!",
                style="bold",
                color="yellow",
            )
            attempt += 1

    if not win:
        printf(
            "HA HA!!! Eu ganhei! Estava pensando no {}".format(draw_num),
            start="\n",
            style="bold",
            color="magenta",
        )
