# 022
# Crie um programa que leia o nome de uma pessoa e mostre:
#   - O nome com todas as letras maiúsculas;
#   - O nome com todas as letras minúsculas;
#   - Quantas letras totais (sem considerar os espaço);
#   - Quantas letras tem o primeiro nome.

if __name__ == "__main__":
    name = str(input("Digite o seu nome completo: ")).strip()

    print(f"\nSeu nome em letras maiúsculas: {name.upper()}")
    print(f"Seu nome em letras minúsculas: {name.lower()}")
    print(f"Quantidade de letras no seu nome: {len(name.replace(" ", ""))}")
    print(f"Quantidade de letras no seu primeiro nome: {len(name.split()[0])}")
