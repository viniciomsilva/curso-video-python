# 098
# Faça um programa que tenha uma função chamada contador, que receba três
# parâmetros: início, fim e passo. E realize a contagem.
# Seu programa deve realizar três contagens através da função criada:
#   - De 1 a 10, de 1 em 1
#   - De 10 a 0, de 2 em 2
#   - Uma contagem personalizada

from time import sleep

from cli.io import printf


def __count(start: int, stop: int, step: int = 1) -> None:
    if step == 0:
        step = 1

    step *= -1 if stop < start and step > 0 else step * 1
    stop += 1 if stop > 0 and step > 0 else stop - 1

    sleep(1)
    printf("START, ", end="")
    sleep(0.5)

    for i in range(start, stop, step):
        printf(f"{i}, ", end="")
        sleep(0.5)

    printf("END!")
    sleep(1)


def run():
    printf("Contagem: 1 - 10. Passo: 1", style="bold", color="cyan")
    __count(1, 10)
    printf("Contagem: 10 - 0. Passo: 2", start="\n", style="bold", color="cyan")
    __count(10, 0, -2)
    printf("Sua vez de escolher:", start="\n", style="bold")

    start = int(input("Início: "))
    stop = int(input("Término: "))
    step = int(input("Passo: "))

    printf(
        "Contagem: {} - {}. Passo: {}".format(
            start, stop, step if step > 0 else step * -1
        ),
        start="\n",
        style="bold",
        color="cyan",
    )
    __count(start, stop, step)
