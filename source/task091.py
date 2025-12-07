# 091
# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios. Guarde esses resultados num dicionário. No final, coloque o
# dicionário em ordem, sabendo que o vencedor foi quem tirou o maior valor.

from time import sleep
from random import randint

from cli.wait import wait


def run():
    players = {}

    # drawing values
    for i in range(4):
        n = randint(1, 6)
        players[f"player{i}"] = n

        print(f"player{i} sorteou: {n}")
        sleep(2)

    # ranking values
    ranking = sorted(players.items(), key=lambda p: p[1], reverse=True)

    # output
    wait("Classificando---------------")
    for i, v in enumerate(ranking):
        print(f"{i + 1}º lugar: {v[0]} >> {v[1]}")
