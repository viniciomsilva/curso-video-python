# 045
# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ.

# REGRAS
#   Pedra quebra a tesoura
#   Papel cobre a pedra
#   Tesoura corta o papel

from random import choice

from cli.io import inputf
from cli.io import printf
from cli.wait import wait
from scripts import terminal

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


def __who_won(usr: str, pc: str):
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

    return result


def run():
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
            msg = "Eu escolhi: {}\n".format(result["pc"])
            msg += "Você escolheu: {}\n\n".format(result["usr"])

            if result["winner"] == "nobody":
                msg += "🤡 {}!".format(result["rule"])
            elif result["winner"] == "usr":
                msg += "🥳 Parabéns! Você ganhou. {}!".format(result["rule"])
            else:
                msg += "🤣 HA HA! Eu ganhei. {}!".format(result["rule"])

            printf(
                msg,
                style="bold",
            )
        except:
            printf(
                "😰 Opção inválida!",
                style="bold",
                color="magenta",
            )
        finally:
            if (
                inputf(
                    "🥺 Quer jogar de novo? [y/n] ",
                    start="\n",
                    style="bold",
                    color="yellow",
                ).lower()
                == "n"
            ):
                break
