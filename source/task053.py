# 053
# Crie um programa que leia uma frase qualquer e mostre se ela é um palíndromo.

from re import sub

from cli.io import printf


def __ispalindrome(x: str):
    txt = sub(r"[^a-z0-9]", "", x.lower())

    return txt[::-1] == txt


def run():
    rps = {
        "color": "",
        "content": "",
    }
    x = input("Digite uma palavra, frase ou número: ")

    rps["content"] = x.capitalize().strip()
    if __ispalindrome(x):
        rps["color"] = "cyan"
        rps["content"] += " é um palíndromo!"
    else:
        rps["color"] = "magenta"
        rps["content"] += " NÃO é um palíndromo!"

    printf(
        rps["content"],
        start="\n",
        style="bold",
        color=rps["color"],
    )
