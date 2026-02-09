# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:  o nome de um jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# funções:
def ficha(nome, gols):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


# programa principal:
print('-'*40)
n = str(input('Nome do Jogador: ')).strip()
if len(n) < 1:
    n = '<desconhecido>'
g = str(input('Número de Gols: '))
if len(g) < 1:
    g = '0'
print(ficha(n, g))