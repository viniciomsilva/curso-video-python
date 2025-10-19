# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from classes.music_player import MusicPlayer
from scripts import terminal
from scripts.custom import customize


def print_playlist(playlist: list):
    terminal.clear()
    print(
        customize(
            "\nMúsicas Disponíveis\n",
            style="bold",
            color="cyan",
        )
    )
    for i, song in enumerate(playlist):
        print(
            "[{:2}] {}, {}".format(
                i + 1,
                str(song["title"]).title(),
                str(song["artist"]).title(),
            ),
        )
    print()


def run():
    player = MusicPlayer()

    while True:
        try:
            print_playlist(player.playlist)
            song = player.select(int(input("Selecione uma música: ")))

            print(
                customize(
                    "Tocando {}, {}".format(
                        str(song["title"]).title(),
                        str(song["artist"]).title(),
                    ),
                    style="bold",
                    color="green",
                )
            )

            player.play()
        except:
            print(
                customize(
                    "\nPor favor! Escolha uma opção válida.",
                    style="bold",
                    color="magenta",
                )
            )
        finally:
            if input("Quer ouvir outra? [y/n]: ") == "n":
                break

    player.quit()
