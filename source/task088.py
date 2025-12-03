# 088
# Faça um programa que ajude um jogados da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
# entre 1 e 60 para cada jogo, cadastrando tudo numa lista composta.

from time import sleep
from random import sample

from cli.io import printf
from cli.wait import wait


def run():
    numbers = range(1, 61)

    quant = int(input("Quantos jogos quer gerar? "))

    wait("Gerando os jogos...")
    for i in range(quant):
        game = sorted(sample(numbers, 6))

        sleep(1)
        print(
            "Jogo #{:<2}: {}".format(
                i + 1,
                ", ".join(map(str, game)),
            )
        )

    printf(
        "🐷 Boa sorte!!!",
        start="\n",
        style="bold",
        color="cyan",
    )
