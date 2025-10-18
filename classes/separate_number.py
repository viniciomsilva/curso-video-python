from scripts import database as db


class SeparateNumber:

    def __init__(self, number: int):
        self.__number = number
        self.__divisor: int = 1
        self.__digits: list = []

        self.__decimal_orders: list = [
            data[0] for data in db.read_csv("decimal_orders.csv")
        ]
        self.__separate()

    @property
    def separated(self) -> list:
        return [
            {"decimal_order": self.__decimal_orders[i], "digit": digit}
            for i, digit in enumerate(self.__digits)
        ]

    @property
    def decimal_orders(self) -> list:
        return self.__decimal_orders

    def __get_digit(self) -> int:
        digit = self.__number // self.__divisor % 10
        self.__divisor *= 10

        return digit

    def __separate(self) -> None:
        length = len(str(self.__number))
        self.__digits = [self.__get_digit() for _ in range(length)]
