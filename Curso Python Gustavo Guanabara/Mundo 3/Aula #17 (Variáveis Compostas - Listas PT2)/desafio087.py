# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# programa:
matriz = [[], [], []]
paresSum = 0
maior2linha = 0
for p in range(0, 3):
    for m in range(0, 3):
        matriz[p].append(int(input(f'Digite um valor para [{p}, {m}]: ')))
print('-=-'*20)
for a in matriz[0]:
    print(f'[  {a}  ]', end = '')
    if a % 2 == 0:
        paresSum += a
print()
for b in matriz[1]:
    print(f'[  {b}  ]', end = '')
    if b > maior2linha:
        maior2linha = b
    if b % 2 == 0:
        paresSum += b
print()
for c in matriz[2]:
    print(f'[  {c}  ]', end = '')
    if c % 2 == 0:
        paresSum += c
print()
print('-=-'*20)
coluna3Sum = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores pares é {paresSum}')
print(f'A soma dos valores da terceira coluna é {coluna3Sum}')
print(f'O maior valor da segunda linha é {maior2linha}')