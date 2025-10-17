from utils import custom as cs


def run():
    print(
        "🌎 {}Hello World!".format(
            cs.customize(style="bold", color="green"),
        )
    )


if __name__ == "__main__":
    run()
