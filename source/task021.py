# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from utils import MusicPlayer
from utils import custom as cs
from utils import terminal as tm


def print_playlist(playlist):
    tm.clear()
    print(cs.colorize("\nMúsicas Disponíveis\n", color="cyan"))
    for i, song in enumerate(playlist):
        print(cs.bold(f"[{(i + 1):3}] {song["title"]} ({song['artist']})"))
    print()


def run():
    player = MusicPlayer()

    print_playlist(player.playlist)

    while True:
        try:
            song = player.select(int(input("Selecione um música: ")))

            print(
                cs.colorize(
                    f"Tocando {song["title"]} ({song['artist']})",
                    color="green",
                )
            )

            player.play()

            if input("Quer ouvir outra? [y/n]: ") != "y":
                player.quit()
                break

            print_playlist(player.playlist)
        except:
            print(
                cs.colorize(
                    "Por favor! Escolha uma opção válida.",
                    color="lilac",
                )
            )


if __name__ == "__main__":
    run()
