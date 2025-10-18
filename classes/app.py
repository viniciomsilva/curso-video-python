from scripts.database import read_csv

import source.hello_world as hello_word
import source.task001 as task001
import source.task002 as task002
import source.task003 as task003


class App:

    def __init__(self) -> None:
        self.__mini_apps: list

        self.__load_mini_apps()

    @property
    def mini_apps(self) -> list:
        return self.__mini_apps

    def __load_mini_apps(self) -> None:
        self.__mini_apps = [
            {
                "mini_app": str(data[0]).title(),
                "description": str(data[1]).capitalize(),
            }
            for data in read_csv(
                ".mini_apps.csv",
                delimiter="|",
            )
        ]

    def execute(self, option) -> None:
        match option:
            case 0:
                hello_word.run()
            case 1:
                task001.run()
            case 2:
                task002.run()
            case 3:
                task003.run()
            case _:
                raise Exception("Mini-app not found.")
