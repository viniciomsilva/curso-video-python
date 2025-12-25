# 045
# Crie um programa que faça o computador jogar Jokenpô.
#   - Regras:
#       - Pedra quebra a tesoura;
#       - Papel cobre a pedra;
#       - Tesoura corta o papel.

from random import choice

from cli.io import inputf
from cli.io import leave
from cli.io import printf
from cli.ux import wait
from cli import terminal


__OPTIONS = {
    "pe": "✊ Pedra",
    "pa": "🖐️ Papel",
    "te": "✌️ Tesoura",
}


__RULES = {
    "pe_wins": "✊ quebra ✌️",
    "pa_wins": "🖐️ cobre ✊",
    "te_wins": "✌️ corta 🖐️",
}


def __who_won(usr: str, pc: str) -> dict[str, str]:
    result = {
        "usr": __OPTIONS[usr],
        "pc": __OPTIONS[pc],
        "winner": "nobody",
        "rule": "Empatou!",
    }

    if usr == pc:
        return result

    match usr:
        case "pe":
            if pc == "te":
                result["winner"] = "usr"
                result["rule"] = __RULES["pe_wins"]
            else:
                result["winner"] = "pc"
                result["rule"] = __RULES["pa_wins"]
        case "pa":
            if pc == "pe":
                result["winner"] = "usr"
                result["rule"] = __RULES["pa_wins"]
            else:
                result["winner"] = "pc"
                result["rule"] = __RULES["te_wins"]
        case "te":
            if pc == "pa":
                result["winner"] = "usr"
                result["rule"] = __RULES["te_wins"]
            else:
                result["winner"] = "pc"
                result["rule"] = __RULES["pe_wins"]
        case _:
            ...

    return result


if __name__ == "__main__":
    while True:
        try:
            terminal.clear()
            printf(
                "{:=^49}".format(" JOKENPÔ "),
                style="bold",
                color="cyan",
            )
            printf(
                "[PE] ✊ Pedra | [PA] 🖐️ Papel | [TE] ✌️ Tesoura",
                style="bold",
            )

            usr = (
                inputf(
                    "Sua opção: ",
                    start="\n",
                    style="bold",
                )
                .lower()
                .strip()
            )
            pc = choice(list(__OPTIONS.keys()))

            wait("JO...", time=1, end="")
            wait("KEN...", time=1, end="")
            wait("PÔ...", time=1)

            result = __who_won(usr, pc)
            msg = f"Eu escolhi: {result["pc"]}\n"
            msg += f"Você escolheu: {result["usr"]}\n\n"

            if result["winner"] == "nobody":
                msg += f"🤡 {result["rule"]}!"
            elif result["winner"] == "usr":
                msg += f"🥳 Parabéns! Você ganhou. {result["rule"]}!"
            else:
                msg += f"🤣 HA HA! Eu ganhei. {result["rule"]}!"

            printf(
                msg,
                style="bold",
            )

            if leave(
                "🥺 Quer jogar de novo? [y/n] ",
                start="\n",
                style="bold",
                color="yellow",
            ):
                break
        except:
            printf(
                "😰 Opção inválida!",
                style="bold",
                color="magenta",
            )
