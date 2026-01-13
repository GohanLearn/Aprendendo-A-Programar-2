# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
total = 0
quantia = num = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if menor == 0:
        menor = num
    else:
        if num < menor:
            menor = num
    total += num
    quantia += 1
    continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
media = total / quantia
print(f'Você digitou {quantia} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')