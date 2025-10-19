from time import sleep

from classes.app import App
from cli.io import printf
from cli.io import inputf
from scripts.terminal import clear


def print_menu(mini_apps) -> None:
    printf(
        "Mini-apps",
        end="\n\n",
        style="bold",
        color="cyan",
    )
    for i, mini_app in enumerate(mini_apps):
        print(
            "[{:3}] {} {}".format(
                i,
                mini_app["mini_app"],
                mini_app["description"],
            )
        )


def main() -> None:
    app = App()

    while True:
        try:
            clear()
            print_menu(app.mini_apps)

            option = int(
                inputf(
                    "Escolha um mini-app: ",
                    start="\n",
                    style="bold",
                    color="yellow",
                )
            )

            if option < 0:
                break

            clear()
            app.execute(option)

            if (
                inputf(
                    "Quer executar outro mini-app? [y/n]: ",
                    start="\n",
                    style="bold",
                    color="yellow",
                )
                == "n"
            ):
                break
        except Exception as e:
            printf(
                e,
                style="bold",
                color="magenta",
            )
            sleep(2)


if __name__ == "__main__":
    main()
