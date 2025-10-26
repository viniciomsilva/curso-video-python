import sys

from classes.app import App
from cli.io import printf
from cli.io import inputf
from cli.wait import wait
from scripts import terminal as tm


def print_menu(mini_apps) -> None:
    printf(
        "Mini-apps",
        end="\n\n",
        style="bold",
        color="cyan",
    )
    for i, mini_app in enumerate(mini_apps):
        print(
            "[{:3}] {}, {}".format(
                i,
                mini_app["mini_app"],
                mini_app["description"],
            )
        )


def main() -> None:
    app = App()
    exit_cmds = ["n", "no", "exit"]
    option = ""

    while True:
        try:
            tm.clear()
            print_menu(app.mini_apps)

            option = (
                inputf(
                    "Escolha um mini-app: ",
                    start="\n",
                    style="bold",
                    color="yellow",
                )
                .lower()
                .strip()
            )

            if not option in exit_cmds:
                tm.clear()
                app.execute(int(option))
        except Exception as e:
            wait(
                e,
                time=2,
                end="\n",
                style="bold",
                color="magenta",
            )
        finally:
            if option in exit_cmds:
                sys.exit()

            if (
                inputf(
                    "Quer executar outro mini-app? [y/n]: ",
                    start="\n",
                    style="bold",
                    color="yellow",
                )
                in exit_cmds
            ):
                sys.exit()


if __name__ == "__main__":
    main()
