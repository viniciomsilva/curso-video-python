from time import sleep

from classes.app import App

from scripts import terminal
from scripts.custom import customize as cs


def print_menu(mini_apps) -> None:
    print(cs("Mini-apps\n", "bold", "cyan"))
    for i, mini_app in enumerate(mini_apps):
        print(
            "[ {:^3} ] {} {}".format(
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

            if (
                input(
                    cs(
                        "\nQuer executar outro mini-app? [y/n] ",
                        color="green",
                    )
                )
                == "n"
            ):
                break
        except Exception as e:
            print(cs(e, "bold", "red"))
            sleep(2)


if __name__ == "__main__":
    main()
