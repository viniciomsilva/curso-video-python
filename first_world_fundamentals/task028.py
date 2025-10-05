# 028
# ESCREVA UM PROGRAMA QUE FAÇA O PC "PENSAR" NUM NÚMERO INTEIRO ENTRE 0 E 5 E
# PEÇA AO USUÁRIO PARA ADIVINHAR O NÚMERO ESCOLHIDO.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU NÃO.

from random import randint

if __name__ == "__main__":
    chosen_number = randint(0, 5)

    num = int(input("EM QUAL NÚMERO ESTOU PENSADO? #"))

    print(
        "PARABÉNS! VOCÊ GANHOU."
        if num == chosen_number
        else f"HA HA! EU GANHEI, ESTAVA PENSANDO EM #{chosen_number}!"
    )
