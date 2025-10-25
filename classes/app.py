from scripts.database import read_csv
from source import hello_world
from source import task001
from source import task002
from source import task003
from source import task004
from source import task005
from source import task006
from source import task007
from source import task008
from source import task009
from source import task010
from source import task011
from source import task012
from source import task013
from source import task014
from source import task015
from source import task016
from source import task017
from source import task018
from source import task019
from source import task020
from source import task021
from source import task022
from source import task023
from source import task024
from source import task025
from source import task026
from source import task027
from source import task028
from source import task029
from source import task030
from source import task031
from source import task032
from source import task033
from source import task034
from source import task035
from source import task036
from source import task037
from source import task038
from source import task039
from source import task041
from source import task043
from source import task044
from source import task045
from source import task046
from source import task047
from source import task048
from source import task050


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
                "description": str(data[1]),
            }
            for data in read_csv(
                ".mini_apps.csv",
                delimiter="|",
            )
        ]

    def execute(self, option) -> None:
        match option:
            case 0:
                hello_world.run()
            case 1:
                task001.run()
            case 2:
                task002.run()
            case 3:
                task003.run()
            case 4:
                task004.run()
            case 5:
                task005.run()
            case 6:
                task006.run()
            case 7:
                task007.run()
            case 8:
                task008.run()
            case 9:
                task009.run()
            case 10:
                task010.run()
            case 11:
                task011.run()
            case 12:
                task012.run()
            case 13:
                task013.run()
            case 14:
                task014.run()
            case 15:
                task015.run()
            case 16:
                task016.run()
            case 17:
                task017.run()
            case 18:
                task018.run()
            case 19:
                task019.run()
            case 20:
                task020.run()
            case 21:
                task021.run()
            case 22:
                task022.run()
            case 23:
                task023.run()
            case 24:
                task024.run()
            case 25:
                task025.run()
            case 26:
                task026.run()
            case 27:
                task027.run()
            case 28:
                task028.run()
            case 29:
                task029.run()
            case 30:
                task030.run()
            case 31:
                task031.run()
            case 32:
                task032.run()
            case 33:
                task033.run()
            case 34:
                task034.run()
            case 35:
                task035.run()
            case 36:
                task036.run()
            case 37:
                task037.run()
            case 38:
                task038.run()
            case 39:
                task039.run()
            case 40:
                task041.run()
            case 41:
                task043.run()
            case 42:
                task044.run()
            case 43:
                task045.run()
            case 44:
                task046.run()
            case 45:
                task047.run()
            case 46:
                task048.run()
            case 47:
                task050.run()
            case _:
                raise Exception("Mini-app not found.")
