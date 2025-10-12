# 028
# ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" NUM NÚMERO INTEIRO ENTRE 0 E 5 E
# PEÇA AO USUÁRIO PARA ADIVINHAR O NÚMERO ESCOLHIDO.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU NÃO.

from time import sleep
from random import randint

from custom import clear
from custom import customize

if __name__ == "__main__":
    win = False
    attempts = 1
    draw_num = randint(1, 10)

    print(
        "\n{}ENTRE 1 E 10, EM QUAL NÚMERO ESTOU PENSADO?{}".format(
            customize(style="bold", color="cyan"), clear()
        )
    )
    print(
        "{}VOCÊ TEM {} TENTATIVAS. BOA SORTE!{}".format(
            customize(color="yellow"), attempts, clear()
        )
    )

    while (not win) and (attempts <= 3):
        num = int(input("\nDIGITE SUA {}º TENTATIVA: #".format(attempts)))

        print(
            "{}PROCESSANDO...{}".format(
                customize(style="bold", color="cyan"),
                clear(),
            )
        )
        sleep(1)

        if num == draw_num:
            print(
                "\n{}PARABÉNS! VOCÊ GANHOU.{}".format(
                    customize(style="bold", color="green"),
                    clear(),
                )
            )

            win = True
            break
        else:
            print(
                "{}HA HA!!! TENTE NOVAMENTE.{}".format(
                    customize(style="bold", color="yellow"),
                    clear(),
                )
            )

        attempts += 1

    if not win:
        print(
            "\n{}HA HA!!! EU GANHEI! ESTAVA PENSANDO NO #{}{}".format(
                customize(style="bold", color="lilac"),
                draw_num,
                clear(),
            )
        )
