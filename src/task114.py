# 114
# Crie um código em Python que teste se o site Pudim está acessível pelo
# computador usado.

from urllib.request import urlopen


def run():
    url = "http://www.pudim.com.br"

    try:
        if urlopen(url):
            print(f"O site: {url} está acessível!")
        else:
            raise
    except:
        print(f"O site: {url} NÃO está acessível!")


if __name__ == "__main__":
    run()
