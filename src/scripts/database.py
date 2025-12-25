from csv import reader
from pathlib import Path


__DATA_PATH = Path.joinpath(
    Path(__file__).parent.parent.parent,
    "data",
).resolve()


def read_csv(
    filename: str,
    mode: str = "r",
    delimiter: str = ",",
) -> list[list[str]]:
    try:
        with open(
            file=Path.joinpath(__DATA_PATH, filename).resolve(),
            mode=mode,
        ) as file:
            data = reader(
                file,
                dialect="excel",
                delimiter=delimiter,
            )
            return [d for d in data]
    except Exception as e:
        print(e)
        return []


def write(
    *args: list[object],
    filename: str,
    mode: str = "w",
) -> bool:
    try:
        with open(
            file=Path.joinpath(__DATA_PATH, filename).resolve(),
            mode=mode,
            encoding="utf-8",
        ) as file:
            for data in args:
                line = ",".join(map(str, data))
                file.write(f"{line}\n")
            return True
    except Exception as e:
        print(e)
        return False


if __name__ == "__main__":
    print(__DATA_PATH)
