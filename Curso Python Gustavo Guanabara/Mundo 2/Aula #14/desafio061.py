# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    cont += 1
    print(termo, end = ' -> ')
    termo += razao
print('FIM')