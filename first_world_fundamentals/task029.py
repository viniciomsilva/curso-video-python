# 029
# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
# SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
# A MULTA VAI CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE.

if __name__ == "__main__":
    speed = float(input("DIGITE A VELOCIDADE DO CARRO (KM/H): "))

    print(
        "TUDO BEM!"
        if speed <= 80
        else "VOCÊ FOI MULTADO EM {:.2f}".format((speed - 80) * 7)
    )
