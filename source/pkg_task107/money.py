def increase(
    value: float,
    percentage: float,
    format: bool = False,
) -> str | float:
    r = value * (1 + percentage / 100)

    return brl(r) if format else r


def decrease(
    value: float,
    percentage: float,
    format: bool = False,
) -> str | float:
    r = value * (1 - percentage / 100)

    return brl(r) if format else r


def double(
    value: float,
    format: bool = False,
) -> str | float:
    r = value * 2

    return brl(r) if format else r


def half(
    value: float,
    format: bool = False,
) -> str | float:
    r = value / 2

    return brl(r) if format else r


def brl(value: float) -> str:
    r = f"R$ {value:,.2f}"

    return r.replace(",", "_").replace(".", ",").replace("_", ".")


def summary(value: float, percentage: float):
    print("\nResumo")
    print(
        ">> {} com {:.1f}% de incremento: {}".format(
            brl(value),
            percentage,
            increase(value, percentage, True),
        )
    )
    print(
        ">> {} com {:.1f}% de decremento: {}".format(
            brl(value),
            percentage,
            decrease(value, percentage, True),
        )
    )
    print(
        ">> A metade de {}: {}".format(
            brl(value),
            half(value, True),
        )
    )
    print(
        ">> O dobro de {}: {}".format(
            brl(value),
            double(value, True),
        )
    )
