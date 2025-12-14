# 104
# Faça um programa que tenha a função leiInt(), que vai funcionar como a função
# input() do Python, validando apenas as entradas numéricas.

from cli.io import printf


def __input_int(prompt: str = "") -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except:
            printf("Por favor! ", end="", color="magenta")


def run():
    num = __input_int("Digite um número: ")

    printf(
        f"😊 Você digitou o número {num}!",
        start="\n",
        style="bold",
        color="cyan",
    )
