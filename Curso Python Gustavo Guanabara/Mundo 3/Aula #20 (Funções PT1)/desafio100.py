# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro de uma lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

# bibliotecas
from random import randint


# listas
números = list()


# funções
def sorteia(núm):
    print('Sorteando 5 valores da lista: ', end = '')
    for u in range(0, 5):
        núm.append(randint(1, 10))
        print(núm[u], end = ' ')
    print('PRONTO!')


def somaPar(núm):
    soma = 0
    for i in núm:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {núm}, temos {soma}')


# programa principal
sorteia(números)
somaPar(números)