# 027
# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA
# O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE


if __name__ == "__main__":
    name = input("DIGITE O SEU NOME COMPLETO: ").upper()

    last_name_pos = len(name.split()) - 1

    print(f"SEU PRIMEIRO NOME É {name.split()[0]}")
    print(f"SEU SOBRENOME É {name.split()[last_name_pos]}")
