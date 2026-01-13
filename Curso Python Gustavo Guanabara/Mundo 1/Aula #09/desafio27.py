# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente.
#Ex: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Primeiro: {nome[0]}')
print(f'Ultimo: {nome[len(nome)-1]}')
