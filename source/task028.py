# 028
# ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" NUM NÚMERO INTEIRO ENTRE 0 E 5 E
# PEÇA AO USUÁRIO PARA ADIVINHAR O NÚMERO ESCOLHIDO.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU NÃO.

from time import sleep
from random import randint

from utils import custom as cs
from utils import terminal as tm


def run():
    win = False
    attempts = 1
    draw_num = randint(1, 10)

    tm.clear()
    print(
        cs.colorize(
            "Entre 0 e 10, em qual número estou pensando?",
            color="cyan",
        )
    )
    print(
        cs.colorize(
            f"Você tem {attempts} tentativas. Boa sorte!",
            color="yellow",
        )
    )

    while not win and attempts <= 3:
        num = int(input(f"\nDigite sua {attempts}º tentativa: "))

        print(
            cs.colorize(
                "Processando...",
                color="green",
            )
        )
        sleep(1)

        if num == draw_num:
            print(
                cs.colorize(
                    "\nParabéns! Você ganhou!",
                    color="green",
                )
            )

            win = True
        else:
            print(
                cs.colorize(
                    "HA HA!!! Tente novamente!",
                    color="yellow",
                )
            )

        attempts += 1

    if not win:
        print(
            cs.colorize(
                f"\nHA HA!!! Eu ganhei! Estava pensando no {draw_num}",
                color="lilac",
            )
        )


if __name__ == "__main__":
    run()
