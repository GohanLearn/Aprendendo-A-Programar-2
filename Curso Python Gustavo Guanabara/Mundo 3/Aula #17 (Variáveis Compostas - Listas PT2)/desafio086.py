# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[], [], []]
for p in range(0, 3):
    for m in range(0, 3):
        matriz[p].append(int(input(f'Digite um valor para [{p}, {m}]: ')))
print('-=-'*20)
for a in matriz[0]:
    print(f'[  {a}  ]', end = '')
print()
for b in matriz[1]:
    print(f'[  {b}  ]', end = '')
print()
for c in matriz[2]:
    print(f'[  {c}  ]', end = '')