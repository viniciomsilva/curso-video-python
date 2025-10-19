# 037
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR INTEIRO QUALQUER E PEÇA PARA O USUÁRIO
# ESCOLHER QUAL SERÁ A BASE NUMÉRICA DE CONVERSÃO:
# 	1 PARA BASE BINÁRIA
# 	2 PARA OCTAL
# 	3 PARA HEXADECIMAL

from time import sleep

from scripts.custom import customize


def run():
    print("Conversor decimal para:")
    print("[2] Binário | [8] Octal | [16] Hexadecimal")

    while True:
        try:
            num = int(input("\nDigite um número inteiro: "))
            base = int(input("Para qual base você quer converter? "))

            print(
                customize(
                    "\nCalculando...\n",
                    style="bold",
                    color="green",
                )
            )
            sleep(1)

            match base:
                case 2:
                    print(
                        customize(
                            "{} em binário = {}".format(
                                num,
                                bin(num)[2:],
                            ),
                            style="bold",
                        )
                    )
                case 8:
                    print(
                        customize(
                            "{} em octal = {}".format(
                                num,
                                oct(num)[2:],
                            ),
                            style="bold",
                        )
                    )
                case 16:
                    print(
                        customize(
                            "{} em hexadecimal = {}".format(
                                num,
                                hex(num)[2:],
                            ),
                            style="bold",
                        )
                    )
                case _:
                    print(
                        customize(
                            "Base de conversão inválida!",
                            style="bold",
                            color="magenta",
                        )
                    )
        except Exception as e:
            print(
                customize(
                    e,
                    style="bold",
                    color="magenta",
                )
            )
        finally:
            if input("\nQuer converter outro? [y/n] ") == "n":
                break
