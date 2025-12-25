# 106
# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai
# digitar um comando e o manual vai aparecer. Quando o usuário digitar a palavra
# FIM, o programa será encerrado.
# Obs.: Use cores!

from cli.io import inputf
from cli.io import printf
from cli.ux import wait
from cli.ux import clear


if __name__ == "__main__":
    while True:
        clear()
        printf(
            "🆘 Sistema de ajuda PyHelp!",
            end="\n\n",
            style="bold",
            color="magenta",
        )
        printf(
            "Digite uma função ou biblioteca.",
            end=" ",
            style="bold",
            color="green",
        )
        printf(
            "(END: Finaliza; Q: Sai do Interactive Help)",
            style="bold",
            color="yellow",
        )

        request = (
            inputf(
                ">>> ",
                style="bold",
                color="green",
            )
            .strip()
            .lower()
            .replace("()", "")
        )

        if request in "end":
            break

        wait(f"Acessando o manual de {request}...")
        help(request)
