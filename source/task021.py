# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from classes.music_player import MusicPlayer
from cli.io import inputf
from cli.io import printf
from scripts.terminal import clear


def print_playlist(playlist: list):
    clear()
    printf(
        "Músicas Disponíveis",
        start="\n",
        end="\n\n",
        style="bold",
        color="cyan",
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
            song = player.select(int(input("Escolha uma música: ")))

            printf(
                "Tocando: {}, {}".format(
                    str(song["title"]).title(),
                    str(song["artist"]).title(),
                ),
                style="bold",
                color="green",
            )

            player.play()
        except:
            printf(
                "Por favor! Escolha uma opção válida.",
                start="\n",
                style="bold",
                color="magenta",
            )
        finally:
            if (
                inputf(
                    "Quer ouvir outra? [y/n]: ",
                    style="bold",
                    color="yellow",
                )
                == "n"
            ):
                break

    player.quit()
