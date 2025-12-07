from datetime import date


class Person:

    def __init__(self, name: str, birth: int, sex: str = "") -> None:
        self.__name = name
        self.__birth = birth
        self.__sex = sex

    @property
    def age(self) -> int:
        return date.today().year - self.__birth

    @property
    def info(self) -> dict:
        return {
            "name": self.__name,
            "age": self.age,
            "sex": self.__sex,
        }
