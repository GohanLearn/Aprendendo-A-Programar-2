# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.

# programa:
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razao
for i in range(primeiro, decimo + razao, razao):
    print(i, end = ' -> ')
print('Acabou')