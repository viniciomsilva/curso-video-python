# 005
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E
# ANTECESSOR

from custom import clear
from custom import customize

if __name__ == "__main__":
    num = int(input("DIGITE UM NÚMERO INTEIRO QUALQUER: "))

    print(
        "{} ANTECESSOR: {:4} {}".format(
            customize(style="bold", back="cyan"),
            (num - 1),
            clear(),
        )
    )
    print(
        "{} SUCESSOR..: {:4} {}".format(
            customize(style="bold", back="lilac"),
            (num + 1),
            clear(),
        )
    )
