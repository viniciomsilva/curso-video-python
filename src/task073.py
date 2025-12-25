# 073
# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#   - Apenas os 5 primeiros colocados
#   - Os últimos 4 colocados da tabela
#   - Uma lista com os nomes em ordem alfabética
#   - Em que posição na tabela está o time Chapecoense

# Dados do Campeonato Brasileiro de 20/nov/2025

from typing import Iterable

from cli.io import inputf_int
from cli.io import inputf
from cli.io import printf
from cli.ux import clear
from scripts.database import read_csv


def __rps(txt: object) -> None:
    printf(
        txt,
        start="\n",
        style="bold",
        color="cyan",
    )


def __show(values: Iterable[str], end: str = "\n") -> None:
    for value in values:
        print(value, end=end)


def __menu() -> None:
    options = (
        "[1] Todos",
        "[2] Cinco Primeiros",
        "[3] Quatro Últimos",
        "[4] Buscar Posição",
        "[5] Ordem Alfabética",
        "[0] Sair",
    )
    __show(options, end=" ")


if __name__ == "__main__":
    teams = tuple([data[0] for data in read_csv("teams.csv")])

    while True:
        __menu()
        option = inputf_int("O que você quer ver? ", start="\n")

        match option:
            case 1:
                __rps("Todos:")
                __show(teams)
            case 2:
                __rps("Os cinco primeiros colocados:")
                __show(teams[:5])
            case 3:
                __rps("Os quatro últimos colocados:")
                __show(teams[-4:])
            case 4:
                team = input("De qual time? ").strip().title()
                __rps(f"O {team} está na {teams.index(team) + 1}ª posição.")
            case 5:
                __rps("Os quatro últimos colocados:")
                __show(sorted(teams))
            case 0:
                break
            case _:
                ...

        inputf(
            "Digite qualquer tecla para continuar...",
            start="\n",
            style="bold",
            color="green",
        )
        clear()
