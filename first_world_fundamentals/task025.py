# 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO
# NOME

if __name__ == "__main__":
    name = input("DIGITE SEU NOME COMPLETO: ").strip().upper()

    if "SILVA" in name:
        print(f"\nPARABÉNS, {name}! VOCÊ É UM SILVA")
    else:
        print(f"\nQUE PENA, {name}! VOCÊ NÃO FAZ PARTE DOS SILVAS")
