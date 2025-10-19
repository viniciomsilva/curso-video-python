from time import sleep

from classes.app import App
from scripts import terminal
from scripts.custom import customize


def print_menu(mini_apps) -> None:
    print(
        customize(
            "Mini-apps\n",
            style="bold",
            color="cyan",
        )
    )
    for i, mini_app in enumerate(mini_apps):
        print(
            "[{:3}] {} {}".format(
                i,
                mini_app["mini_app"],
                mini_app["description"],
            ),
        )


def main() -> None:
    app = App()

    while True:
        try:
            terminal.clear()
            print_menu(app.mini_apps)

            option = int(input("\nEscolha um mini-app: "))

            if option < 0:
                break

            terminal.clear()
            app.execute(option)

            if input("\nQuer executar outro mini-app? [y/n]: ") == "n":
                break
        except Exception as e:
            print(
                customize(
                    e,
                    style="bold",
                    color="magenta",
                )
            )
            sleep(2)


if __name__ == "__main__":
    main()
