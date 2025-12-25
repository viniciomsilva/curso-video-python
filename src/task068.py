# 068
# Faça um programa que jogue par ou ímpar com o computador. O jogo só será
# interrompido quando o jogador PERDER, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint

from cli.io import inputf_int
from cli.io import printf


if __name__ == "__main__":
    victories = 0
    pc = 0
    me = {
        "option": 0,
        "num": 0,
    }
    total = 0

    while True:
        try:
            pc = randint(1, 10)
            num = inputf_int("Qual número você escolhe? ")
            option = input("Par ou Ímpar? [P/I] ").strip()[0]

            if option in "Pp":
                option = 0
            elif option in "Ii":
                option = 1
            else:
                raise Exception("Digite uma opção válida!!!")

            me["num"] = num
            me["option"] = option
            total = pc + me["num"]

            if total % 2 == me["option"]:
                victories += 1
            else:
                break
        except Exception as e:
            printf(
                e,
                style="bold",
                color="magenta",
            )
        finally:
            printf(
                "Resultado: VOCÊ [{}] - PC [{}] - TOTAL: [{}]".format(
                    me["num"],
                    pc,
                    total,
                ),
                end="\n\n",
                style="bold",
            )

    if victories > 0:
        printf(
            f"🥳 Parabéns! Você ganhou {victories} vezes!",
            style="bold",
            color="cyan",
        )
    else:
        printf(
            "🤡 Ha Ha! Você não ganhou nenhuma vez!",
            style="bold",
            color="magenta",
        )
