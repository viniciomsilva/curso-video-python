from csv import reader
from pathlib import Path


DATA_PATH = Path.joinpath(Path(__file__).parent.parent, "data").resolve()


def read_csv(filename: str, mode: str = "r", delimiter: str = ",") -> list:
    try:
        with open(
            file=Path.joinpath(DATA_PATH, filename).resolve(),
            mode=mode,
        ) as file:
            return list(
                reader(
                    file,
                    dialect="excel",
                    delimiter=delimiter,
                )
            )
    except Exception as e:
        print(e)
        return []


def write(*args, filename: str, mode: str = "w") -> bool:
    try:
        with open(
            file=Path.joinpath(DATA_PATH, filename).resolve(),
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
