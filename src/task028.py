# 028
# Escreva um programa que faça o pc "pensar" num número inteiro entre 0 e 5 e
# peça ao usuário para adivinhar o número escolhido.
# O programa deverá escrever na tela se o usuário venceu ou não.

# 058
# Melhore o jogo do DESAFIO 28 onde o computador vai pensar num número entre 0 e
# 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no
# final quantos palpites foram necessários para vencer.

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


if __name__ == "__main__":
    run()
