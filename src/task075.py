# 075
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os numa
# tupla. No final, mostre:
#   - Quantas vezes apareceu o valor 9
#   - Em que posição foi digitado o primeiro valor 3
#   - Quais foram os números pares

# 081
# Crie um programa que vai ler vários números e colocá-los numa lista.
# Depois disso mostre:
#   - Quantos números foram digitados
#   - A lista de valores ordenada de forma decrescente
#   - Se o valor 5 foi digitado e está ou não na lista

# 082
# Crie um programa que vai ler vários números e colocá-los numa lista.
# Depois disso, crie duas listas que vão conter apenas os valores pares
# e ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.

# 085
# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os numa lista única que mantenha separados os valores pares e
# ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

from cli.io import inputf_int
from cli.io import leave
from cli.io import printf


if __name__ == "__main__":
    msg = ""
    numbers: list[int] = []

    while True:
        n = inputf_int("Digite um número inteiro: ", start="\n")

        numbers.append(int(n))

        if leave("Quer adicionar outros? [S/N] "):
            break

    even = set(filter(lambda n: n % 2 == 0, numbers))
    odd = set(filter(lambda n: n % 2 != 0, numbers))

    msg += f"A lista completa: {numbers}"
    msg += f"A lista completa tem {numbers.__len__()} números."
    msg += f"\nO número 5 aparece {numbers.count(5)} vez(es)!"
    msg += f"\nO número 9 aparece {numbers.count(9)} vez(es)!"

    if 3 in numbers:
        msg += f"\nO primeiro 3 está na {numbers.index(3) + 1}ª posição!"
    else:
        msg += "\nO números 3 não está na lista!"

    msg += f"\nEm ordem decrescente: {sorted(numbers, reverse=True)}"
    msg += f"\nOs números pares são: {sorted(even)}!"
    msg += f"\nOs números ímpares são: {sorted(odd)}!"

    printf(msg, start="\n", style="bold")
