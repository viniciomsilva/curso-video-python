from csv import reader
from pathlib import Path


DATA_PATH = Path.joinpath(Path(__file__).parent.parent, "data").resolve()


def read_csv(filename: str) -> list:
    with open(Path.joinpath(DATA_PATH, filename).resolve()) as file:
        return list(reader(file))
