# 083
# Crie um programa onde o usuário digite uma expressão matemática qualquer que
# use parênteses. Seu aplicativo deverá analisar se a expressão passada está com
# os parênteses abertos e fechados na ordem correta.

from asteval import Interpreter  # type: ignore


if __name__ == "__main__":
    aeval = Interpreter()

    while True:
        try:
            exp = input("Digite uma expressão algébrica: ").strip().lower()

            if exp.count("(") == exp.count(")"):
                rs = aeval(exp)  # type: ignore
                break

            raise
        except:
            print("Por favor! ", end=" ")

    print("A expressão é válida!")
    print(f"E o resultado é: {rs}")
