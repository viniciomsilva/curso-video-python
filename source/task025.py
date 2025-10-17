# 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO
# NOME

from utils import custom as cs


def run():
    name = input("Digite o seu nome completo: ").strip().lower()

    if "silva" in name:
        print(
            cs.colorize(
                "Parabéns! Você é um(a) Silva",
                color="cyan",
            )
        )
    else:
        print(
            cs.colorize(
                "Que pena! Você NÃO faz parte dos Silvas",
                color="cyan",
            )
        )


if __name__ == "__main__":
    run()
