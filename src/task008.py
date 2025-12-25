# 008
# Escreva um programa que leia um valor em metros e mostre-o em centímetros e
# milímetros.

from cli.io import inputf_flo


if __name__ == "__main__":
    num = inputf_flo("Digite um valor em metros: ")

    print("Em quilômetros: {}km".format(num / 1000))
    print("Em hectômetros: {}hm".format(num / 100))
    print("Em decâmetros.: {}dac".format(num / 10))
    print("Em decímetros.: {:.0f}dc".format(num * 10))
    print("Em centímetros: {:.0f}cm".format(num * 100))
    print("Em milímetros.: {:.0f}mm".format(num * 1000))
