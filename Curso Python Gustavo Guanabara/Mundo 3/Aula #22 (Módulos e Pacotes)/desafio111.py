# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.

# Transfira todas as funções utilizadas nos desafios 107, 108, 109 para o primeiro pacote e mantenha tudo funcionando.

# imports:
from ex111.utilidadesCeV import moeda


# programa principal:
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)