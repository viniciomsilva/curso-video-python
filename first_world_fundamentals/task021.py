# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from classes.music_player import MusicPlayer
from custom import clear
from custom import customize

if __name__ == "__main__":
    player = MusicPlayer()

    print(
        "\n{}MÚSICAS DISPONÍVEIS{}\n".format(
            customize(style="bold", color="cyan"),
            clear(),
        )
    )
    for i, song in enumerate(player.playlist):
        print(
            "{}#{:3}{}{} {} - {}{}".format(
                customize(style="bold", color="green"),
                (i + 1),
                clear(),
                customize(style="bold"),
                song["title"],
                song["artist"],
                clear(),
            )
        )
    print()

    while True:
        try:
            song = player.select(int(input("SELECIONE UMA MÚSICA: # ")))

            print(
                "{}ESTÁ TOCANDO AGORA: {} - {}{}".format(
                    customize(style="bold", color="green"),
                    song["title"],
                    song["artist"],
                    clear(),
                )
            )

            player.play()

            if input("QUER OUVIR OUTRA? [y/n]: ") != "y":
                player.quit()
                break

            print()
        except:
            print(
                "\n{}POR FAVOR!{}".format(
                    customize(style="bold", color="lilac"),
                    clear(),
                )
            )
