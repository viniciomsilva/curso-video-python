# 028
# ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" NUM NÚMERO INTEIRO ENTRE 0 E 5 E
# PEÇA AO USUÁRIO PARA ADIVINHAR O NÚMERO ESCOLHIDO.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU NÃO.

from time import sleep
from random import randint

from scripts import terminal
from scripts.custom import customize


def run():
    win = False
    attempts = 3
    draw_num = randint(1, 10)

    terminal.clear()
    print(
        customize(
            "Entre 0 e 10, em qual número estou pensando?",
            style="bold",
            color="cyan",
        )
    )
    print(
        customize(
            "Você tem {} tentativas. Boa sorte!".format(attempts),
            style="bold",
            color="yellow",
        )
    )

    while not win and attempts > 0:
        num = int(
            input(
                "\nDigite sua {}º tentativa: ".format(
                    attempts,
                )
            )
        )

        print(
            customize(
                "Processando...",
                style="bold",
                color="green",
            )
        )
        sleep(1)

        if num == draw_num:
            print(
                customize(
                    "\n🥳 Parabéns! Você ganhou!",
                    style="bold",
                    color="green",
                )
            )
            win = True
        else:
            print(
                customize(
                    "HA HA!!! Tente novamente!",
                    style="bold",
                    color="yellow",
                )
            )
        attempts -= 1

    if not win:
        print(
            customize(
                "\nHA HA!!! Eu ganhei! Estava pensando no {}".format(draw_num),
                style="bold",
                color="magenta",
            )
        )
