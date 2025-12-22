# 043
# DESENVOLVA UM PROGRAMA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE O IMC
# E MOSTRE O STATUS DE ACORDO COM A TABELA ABAIXO:
# 	- ABAIXO DE 18.5:	ABAIXO DO PESO
# 	- ENTRE 18.5 E 25:	PESO IDEAL
# 	- 25 ATÉ 30:		SOBREPESO
# 	- 30 ATÉ 40:		OBESIDADE
# 	- ACIMA DE 40:		OBESIDADE MÓRBIDA

from cli.io import printf
from cli.wait import wait


def __calc(w, h):
    return w / pow(h, 2)


def run():
    msg = {
        "color": "",
        "content": "",
    }

    weight = float(input("Peso (kg): "))
    height = float(input("Altura (m): "))

    wait("Calculando...")

    imc = __calc(weight, height)
    msg["content"] = "Seu IMC é de {}. ".format(round(imc, 1))

    if imc < 18.5:
        msg["color"] = "yellow"
        msg["content"] += "Você está MUITO MAGRO."
    elif imc < 25:
        msg["color"] = "cyan"
        msg["content"] += "Parabéns! Você está com o PESO IDEAL."
    elif imc < 30:
        msg["color"] = "yellow"
        msg["content"] += "Cuidado! Você está SOBREPESO."
    elif imc < 40:
        msg["color"] = "magenta"
        msg["content"] += "Procure um médico! Você está OBESO."
    else:
        msg["color"] = "red"
        msg["content"] += "TRATE-SE JÁ!!! Você tem OBESIDADE MÓRBIDA."

    printf(
        msg["content"],
        style="bold",
        color=msg["color"],
    )


if __name__ == "__main__":
    run()
