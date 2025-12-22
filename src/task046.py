# 046
# FAÇA UM PROGRAMA QUE MOSTRE A CONTAGEM REGRESSIVA PARA A QUEIMA DE FOGOS DE
# ARTIFÍCIO, INDO DE 10 A 0 COM PAUSA DE 1 SEGUNDO.

from time import sleep

from cli.io import printf


def run():
    seconds = int(input("Quantidade de segundos: "))

    if seconds > 30:
        seconds = 30

    for i in range(seconds, 0, -1):
        print(
            f"{i}{" " * 4}",
            end="\r",
        )
        sleep(1)

    printf(
        "🎉 🎉 🎉",
        start="\n",
    )


if __name__ == "__main__":
    run()
