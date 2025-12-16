# 107
# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(),
# diminuir(), dobro() e metade().
# Faça também um programa que importe esses módulo e use algumas dessas funções.

# 108
# Adapte o código do desafio 107, criando uma função adicional chamada moeda()
# que consiga mostrar os valores como monetários formatados.

# 109
# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um
# parâmetro a mais, informando se o valor retornado por elas vai ser ou não
# formatado pela função moeda(), desenvolvida no desafio 108.

# 110
# Adicione ao módulo moeda.py, criado nos desafios anteriores, uma função
# chamada resumo(), que mostra na tela algumas informações geradas pelas funções
# que já temos nos módulo criado até aqui.

# 111
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
# moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o
# primeiro pacote e mantenha tudo funcionando.

# 112
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo
# chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de
# funcionar como a função input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários.

from .pkg_task107.money import summary
from .pkg_task107.validate import read_float


def run():
    v = read_float("Valor: R$ ")
    p = read_float("Percentual (%): ")

    summary(v, p)
