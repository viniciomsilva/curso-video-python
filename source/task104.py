# 104
# Faça um programa que tenha a função leiInt(), que vai funcionar como a função
# input() do Python, validando apenas as entradas numéricas.

# 113
# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a
# possibilidade da digitação de uma número inválido. Aproveite e crie também uma
# função leiaFloat() com a mesma funcionalidade.

from cli.io import inputf_int
from cli.io import inputf_flo


def run():
    print("Tratamento de erro na entrada de números inteiros...")
    num_int = inputf_int("Digite um número inteiro: ")
    print(f"Valor inteiro digitado: {num_int}")

    print("\nTratamento de erro na entrada de números decimais...")
    num_flo = inputf_flo("Digite um número decimal: ")
    print(f"Valor decimal digitado: {num_flo}")
