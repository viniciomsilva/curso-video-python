# 031
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. CALCULE O
# PREÇO DA PASSAGEM, COBRANDO R$ 0,50 POR KM PARA VIAGENS DE ATÉ 200KM E R$ 0,45
# POR KM PARA VIAGENS MAIS DISTANTES.

if __name__ == "__main__":
    distance = float(input("DIGITE A DISTÂNCIA DA VIAGEM (KM): "))

    ticket_price = distance * 0.45 if distance > 200 else distance * 0.5

    print("O VALOR DA PASSAGEM É R${:.2f}".format(ticket_price))
