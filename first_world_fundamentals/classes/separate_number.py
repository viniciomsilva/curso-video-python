from csv import reader
from re import sub
from pathlib import Path


class SeparateNumber:

    def __init__(self, number: int):
        self.__number = number
        self.__divisor: int = 1
        self.__digits: list[int]

        self.__decimal_orders: list[str] = [
            data[0] for data in self.__get_decimal_orders()
        ]
        self.__separate()

    @property
    def separated(self) -> list:
        return [
            {"decimal_order": self.__decimal_orders[i], "digit": digit}
            for i, digit in enumerate(self.__digits)
        ]

    def __get_decimal_orders(self) -> list:
        with open(
            Path(__file__)
            .parent.parent.joinpath("assets", "decimal_orders.csv")
            .resolve(),
        ) as file:
            return list(reader(file))

    def __get_digit_value(self) -> int:
        digit = self.__number // self.__divisor % 10
        self.__divisor *= 10

        return digit

    def __separate(self) -> None:
        length = len(str(self.__number))
        self.__digits = [self.__get_digit_value() for _ in range(length)]
