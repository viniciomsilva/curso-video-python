# 043
# Desenvolva um programa que leia o peso e a altura de uma pessoa, calcule o imc
# e mostre o status de acordo com a tabela abaixo:
#   - Abaixo de 18.5 (abaixo do peso);
#   - Entre 18.5 e 25 (peso ideal);
#   - 25 até 30 (sobrepeso);
#   - 30 até 40 (obesidade);
#   - Acima de 40 (obesidade mórbida).

from cli.io import inputf_flo
from cli.io import printf
from cli.ux import wait


def __calc(w: float, h: float) -> float:
    return w / pow(h, 2)


if __name__ == "__main__":
    msg = {
        "color": "",
        "content": "",
    }

    weight = inputf_flo("Peso (kg): ")
    height = inputf_flo("Altura (m): ")

    wait("Calculando...")

    imc = __calc(weight, height)
    msg["content"] = f"Seu IMC é de {round(imc, 1)}. "

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
