# 035
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS SEGMENTOS DE RETA E DIGA
# AO USUÁRIO SE ELES PODEM OU NÃO FORMAR UM TRIÂNGULO.

# REGRA DA DESIGUALDADE TRIANGULAR
#   A SOMA DE DOIS QUAISQUER SEGMENTOS DEVE SER MAIOR QUE O TERCEIRO

if __name__ == "__main__":
    seg1 = float(input("DIGITE O VALOR DO 1º SEGMENTO: "))
    seg2 = float(input("DIGITE O VALOR DO 2º SEGMENTO: "))
    seg3 = float(input("DIGITE O VALOR DO 3º SEGMENTO: "))

    print(
        "FORMAM UM TRIÂNGULO!"
        if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1
        else "NÃO FORMAM UM TRIÂNGULO!"
    )
