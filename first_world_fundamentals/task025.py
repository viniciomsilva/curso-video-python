# 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO
# NOME

from custom import customize

if __name__ == "__main__":
    name = input("DIGITE SEU NOME COMPLETO: ").upper().strip()

    if "SILVA" in name:
        print(
            "\n{}PARABÉNS, {}! VOCÊ É UM(A) SILVA.".format(
                customize(style="bold", color="cyan"), name
            )
        )
    else:
        print(
            "\n{}QUE PENA, {}! VOCÊ NÃO FAZ PARTE DOS SILVAS.".format(
                customize(style="bold", color="lilac"), name
            )
        )
