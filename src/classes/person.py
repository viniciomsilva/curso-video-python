from cli.ux import THIS_YEAR


class Person:

    def __init__(self, name: str, birth: int, sex: str = "") -> None:
        self.__name = name
        self.__birth = birth
        self.__sex = sex

    @property
    def age(self) -> int:
        return THIS_YEAR - self.__birth

    @property
    def info(self) -> dict[str, str | int]:
        return {
            "name": self.__name,
            "age": self.age,
            "sex": self.__sex,
        }
