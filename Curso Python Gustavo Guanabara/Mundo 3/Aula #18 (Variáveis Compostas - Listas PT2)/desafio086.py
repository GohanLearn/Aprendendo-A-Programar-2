# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

#programa:

## matriz = [[], [], []] # modelo antigo que eu usei
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-'*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
##for a in matriz[0]:
##    print(f'[  {a}  ]', end = '')
##print()
##for b in matriz[1]:
##    print(f'[  {b}  ]', end = '')
##print()
##for c in matriz[2]:
##    print(f'[  {c}  ]', end = '')