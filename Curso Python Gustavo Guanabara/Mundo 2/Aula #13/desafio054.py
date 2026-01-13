# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# programa:

# importando bibliotecas:
from datetime import date

# lendo:
ano = int(date.today().year)
maiores = 0
menores = 0
for i in range(0, 7):
    nascimento = int(input(f'Digite a data de nascimento da {i+1}ª pessoa: '))
    if ano - nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print(f"""Maiores: {maiores}
Menores: {menores}""")