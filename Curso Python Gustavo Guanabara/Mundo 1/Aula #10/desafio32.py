# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# importando bibliotecas
from datetime import date

# obtendo ano
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))

# calculando e respondendo
if ano == 0:
    ano = date.today().year
    if ( (ano % 400) == 0 ) or ( (ano % 4 == 0) and (ano % 100 != 0) ):
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')