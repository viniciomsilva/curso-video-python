# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from pathlib import Path

from classes import MusicPlayer


if __name__ == "__main__":
    player = MusicPlayer()

    player.init()
    player.load(str(Path(__file__).parent.joinpath(
        "media", "task021_songs"
    ).resolve()))
    player.print_playlist()

    while True:
        option = int(input("SELECIONE UMA MÚSICA: #"))
        selected = player.select(option)

        print(f"ESTÁ TOCANDO AGORA: {selected.title} - {selected.artist}")
        player.play(60)  # default duration: 60 seconds

        if input("QUER OUVIR OUTRA? [y/n]: ") != "y":
            player.quit()
            break
        print()
