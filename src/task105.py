# 105
# Faça um programa que tenha uma função chamada notas() que pode receber várias
# notas de alunos e vai retornar um dicionário com as seguintes informações:
#   - Quantidade de notas
#   - A maior nota
#   - A menor nota
#   - A média da turma
#   - A situação (opcional)
# Obs.: Adicione também as DocStrings da função.

from statistics import mean


def __avg(*grades, status: bool = False) -> dict:
    """Calculate average of a classroom.

    Args:
        grades (tuple[float]): N grades.
        status (bool, optional): Status of the classroom. Defaults to False.

    Returns:
        dict: A summary of classroom data: number of grades; highest grade;
        lowest grade; class average; and status.

    Examples:
        >>> __avg(2.5, 6, 9, 7, status=True)
        >>> {'len': 4, 'highest': 9, 'lowest': 2.5, 'mean': 6.125,
            'status': 'REGULAR'}
        >>> __avg(2.5, 6, 9, 7)
        >>> {'len': 4, 'highest': 9, 'lowest': 2.5, 'mean': 6.125}
    """

    m = mean(grades)
    r = {
        "len": len(grades),
        "highest": max(grades),
        "lowest": min(grades),
        "mean": m,
    }

    if status:
        if m >= 7:
            r["status"] = "GOOD"
        elif m >= 5:
            r["status"] = "REGULAR"
        else:
            r["status"] = "BAD"

    return r


def run():
    print(__avg(2.5, 6, 9, 7, status=True))


if __name__ == "__main__":
    run()
