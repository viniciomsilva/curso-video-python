# 037
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR INTEIRO QUALQUER E PEÇA PARA O USUÁRIO
# ESCOLHER QUAL SERÁ A BASE NUMÉRICA DE CONVERSÃO:
# 	1 PARA BASE BINÁRIA
# 	2 PARA OCTAL
# 	3 PARA HEXADECIMAL

from cli.io import inputf
from cli.io import printf
from cli.wait import wait


def run():
    print("Conversor decimal para:")
    print("[2] Binário | [8] Octal | [16] Hexadecimal")

    while True:
        try:
            num = int(input("\nDigite um número inteiro: "))
            base = int(input("Para qual base você quer converter? "))

            wait("Convertendo...")

            match base:
                case 2:
                    printf(
                        "{} em binário: {}".format(num, bin(num)[2:]),
                        style="bold",
                    )
                case 8:
                    printf(
                        "{} em octal: {}".format(num, oct(num)[2:]),
                        style="bold",
                    )
                case 16:
                    printf(
                        "{} em hexadecimal: {}".format(num, hex(num)[2:]),
                        style="bold",
                    )
                case _:
                    printf(
                        "Base de conversão inválida!",
                        style="bold",
                        color="magenta",
                    )
        except Exception as e:
            printf(
                e,
                style="bold",
                color="magenta",
            )
        finally:
            if (
                inputf(
                    "\nQuer converter outro? [y/n] ",
                    style="bold",
                    color="yellow",
                )
                == "n"
            ):
                break


if __name__ == "__main__":
    run()
