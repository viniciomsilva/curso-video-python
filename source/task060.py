# 060
# Faça um programa que leia um número qualquer e mostre o fatorial.
#   Ex.: 5! => 5 * 4 * 3 * 2 * 1 => 120

# 102
# Crie um programa que tenha uma função chamada fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular; e o segundo chamado
# show, que será um valor lógico (opcional), indicando se será mostrado, ou não,
# o processo de cálculo.

from cli.io import printf
from cli.wait import wait


def __factorial(num: int, show: bool = False) -> str:
    """Calculate the factorial of a number n.

    Args:
        num (int): Number to be calculate.
        show (bool, optional): Show the calculation. Defaults to False.

    Returns:
        str: Factorial result.

    Examples:
        __factorial(4) -> '4! = 24'
        __factorial(4, True) -> '4! = 4 * 3 * 2 * 1 = 24'
    """
    from math import factorial as fc

    r = f"{num}! = "

    if show:
        r += " * ".join(map(str, range(num, 1, -1)))
        r += " * 1 = "

    r += f"{fc(num)}"

    return r


def run():
    num = int(input("Digite um número: "))
    show = bool(input("Quer ver o cálculo? "))

    wait("Calculando...")
    printf(
        __factorial(num, show),
        style="bold",
        color="cyan",
    )
