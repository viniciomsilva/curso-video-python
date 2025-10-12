# 014
# ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA EM ºC PARA ºF

from custom import clear
from custom import customize

if __name__ == "__main__":
    celsius = float(input("DIGITE A TEMPERATURA EM ºC: "))

    print(
        "{}{:.1f}ºC{} = {}{:.1f}ºF".format(
            customize(style="bold", color="lilac"),
            celsius,
            clear(),
            customize(style="bold", color="cyan"),
            (celsius * 9 / 5 + 32),
        )
    )
