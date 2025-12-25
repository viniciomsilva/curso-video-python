# 037
# Escreva um programa que leia um valor inteiro qualquer e peça para o usuário
# escolher qual será a base numérica de conversão:
#   - 1 (binária);
#   - 2 (octal);
#   - 3 (hexadecimal).

from cli.io import inputf_int
from cli.io import leave
from cli.io import printf
from cli.ux import wait


if __name__ == "__main__":
    print("Conversor decimal para:")
    print("[2] Binário | [8] Octal | [16] Hexadecimal")

    while True:
        try:
            num = inputf_int("\nDigite um número inteiro: ")
            base = inputf_int("Para qual base você quer converter? ")

            wait("Convertendo...")

            match base:
                case 2:
                    printf(
                        f"{num} em binário: {bin(num)[2:]}",
                        style="bold",
                    )
                case 8:
                    printf(
                        f"{num} em octal: {oct(num)[2:]}",
                        style="bold",
                    )
                case 16:
                    printf(
                        f"{num} em hexadecimal: {hex(num)[2:]}",
                        style="bold",
                    )
                case _:
                    printf(
                        "Base de conversão inválida!",
                        style="bold",
                        color="magenta",
                    )

            if leave(
                "Quer converter outro? [y/n] ",
                start="\n",
                style="bold",
                color="yellow",
            ):
                break
        except Exception as e:
            printf(
                e,
                style="bold",
                color="magenta",
            )
