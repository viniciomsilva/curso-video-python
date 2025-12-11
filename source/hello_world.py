# 000
# Hello World!

# 097
# Faça um programa que tenha uma função chama escreva, que receba um texto
# qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Ex.:
# escreva("Olá, Mundo!")

# Saída:
# ~~~~~~~~~~~~~~~
#   Olá, Mundo!
# ~~~~~~~~~~~~~~~

from cli.io import printf
from scripts.custom import customize


def __title(msg: str):
    line = customize(("~" * (len(msg) + 4)), style="bold", color="cyan")

    printf(line)
    printf(f"  {msg}", style="bold")
    printf(line)


def run():
    __title("Hello World!")
    __title("Vinicio Silva!")
    __title("Curso de Python no YouTube: Curso em Vídeo!")
