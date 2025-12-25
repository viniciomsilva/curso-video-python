# 021
# Faça um programa em python que abra e reproduza um áudio de um arquivo MP3.

from classes.music_player import MusicPlayer
from cli.io import inputf_int
from cli.io import leave
from cli.io import printf
from cli.terminal import clear


def __print_playlist(playlist: list[dict[str, str]]) -> None:
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


if __name__ == "__main__":
    player = MusicPlayer()

    while True:
        try:
            __print_playlist(player.playlist)

            op = inputf_int("Escolha uma música: ")
            song = player.select(op)

            printf(
                "Tocando: {}, {}".format(
                    song["title"].title(),
                    song["artist"].title(),
                ),
                style="bold",
                color="green",
            )

            player.play()

            if leave(
                "Quer ouvir outra? [y/n]: ",
                style="bold",
                color="yellow",
            ):
                break
        except:
            printf(
                "Por favor! Escolha uma opção válida.",
                start="\n",
                style="bold",
                color="magenta",
            )

    player.quit()
