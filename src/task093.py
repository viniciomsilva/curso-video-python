# 093
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluído o total de gols
# feitos durante o campeonato.

# 095
# Aprimore o DESAFIO 093 para que ele funciona com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.

# 103
# Faça um programa que tenha uma função chamada ficha(), que receba dois
# parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

from cli.io import inputf
from cli.io import inputf_int
from cli.io import leave
from cli.io import printf
from cli.ux import wait
from cli import terminal as tm


def __print_players(players: list[dict[str, str | int | list[int]]]) -> None:
    tm.clear()
    printf(
        "Jogadores",
        end="\n\n",
        style="bold",
        color="cyan",
    )
    print(
        "{:4} | {:20} | {:8} | {:5}".format(
            "Cod.",
            "Nome",
            "Partidas",
            "Total",
        )
    )

    for i, p in enumerate(players):
        print(
            "{:<4} | {:20} | {:^8} | {:^5}".format(
                i,
                p["name"],
                p["matches"],
                p["total"],
            )
        )


def __print_player_data(player: dict[str, str | int | list[int]]) -> None:
    tm.clear()
    printf(f"Resumo dos gols do jogador: {player["name"]}", style="bold")
    print(f"Quantidade de partidas jogadas: {player["matches"]}")
    print("Gols por partida: ")

    for i, g in enumerate(player["goals"]):  # type: ignore
        print(f"  > {i + 1}ª partida: {g} gol(s) feito(s)")  # type: ignore


if __name__ == "__main__":
    players: list[dict[str, str | int | list[int]]] = []

    # input
    while True:
        printf("Novo jogador", style="bold")

        name = input("Nome: ").strip()
        matches = inputf_int("N.º de partidas: ")

        goals: list[int] = []

        for i in range(matches):
            n = inputf_int(f"  > N.º de gols na {i + 1}º partida: ")
            goals.append(n)

        players.append(
            {
                "name": name.title() if name else "<empty>",
                "matches": matches,
                "goals": goals,
                "total": sum(goals),
            }
        )

        if leave(
            "Cadastrar outro jogador? [S/N] ",
            start="\n",
            style="bold",
            color="yellow",
        ):
            break

        tm.clear()

    # output
    while True:
        __print_players(players)

        opt = inputf_int(
            "Ver mais detalhes do jogador (-1 para sair): ",
            start="\n",
        )

        if opt == -1:
            break
        elif opt < len(players):
            __print_player_data(players[opt])
            inputf(
                "Pressione qualquer tecla para continuar...",
                start="\n",
                style="bold",
                color="yellow",
            )
            continue
        wait(
            "Desculpe! Opção inválida. Tente novamente!",
            end="\n",
            color="magenta",
        )
