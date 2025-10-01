# 022
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE:
#   O NOME COM TODAS AS LETRAS MAIÚSCULAS
#   O NOME COM TODAS AS LETRAS MINÚSCULAS
#   QUANTAS LETRAS TOTAIS (SEM CONSIDERAR OS ESPAÇO)
#   QUANTAS LETRAS TEM O PRIMEIRO NOME

if __name__ == "__main__":
    name = input("\nDIGITE SEU NOME: ")

    print()
    print(f"SEU NOME EM LETRAS MAIÚSCULAS........: {name.strip().upper()}")
    print(f"SEU NOME EM LETRAS MINÚSCULAS........: {name.strip().lower()}")
    print(
        f"QUANTIDADE LETRAS NO SEU NOME........: {len(name.replace(" ", ""))}"
    )
    print(f"QUANTIDADE DE LETRAS NO PRIMEIRO NOME: {len(name.split()[0])}")
