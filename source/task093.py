# 093
# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será guardado em um dicionário, incluído o total de gols
# feitos durante o campeonato.


def run():
    player = {}

    player["name"] = input("Nome: ").strip().title()
    player["matches"] = int(input("N.º de partidas: "))

    player["goals"] = []

    for i in range(player["matches"]):
        goals = int(input(f"  > N.º de gols na {i + 1}º partida: "))
        player["goals"].append(goals)

    player["utilization"] = sum(player["goals"])

    # output
    print("-" * 30)
    print(f"Dados do jogador: {player['name']}")
    print(f"Quantidade de gols: {player['utilization']}")
    print(f"Quantidade de partidas: {player['matches']}")
    print(f"Gols por partida: ")
    for i, v in enumerate(player["goals"]):
        print(f"  > {i + 1}ª partida: {v}")
