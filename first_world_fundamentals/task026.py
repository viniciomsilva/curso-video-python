# 026
# CRIE UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
#   QUANTAS VEZES APARECEM A LETRA 'A'
#   EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#   EM QUE POSIÇÃO ELA APARECE A ULTIMA VEZ


if __name__ == "__main__":
    phrase = input("DIGITE UMA FRASE QUALQUER: ").strip().lower()

    first = phrase.find("a")
    last = phrase.rfind("a")

    print(f"QUANTIDADE DE 'A': {phrase.count("a")}")
    print(f"PRIMERO 'A'......: {first + 1 if first > 0 else "NaN"}")
    print(f"ULTIMO 'A'.......: {last + 1 if last > 0 else "NaN"}")
