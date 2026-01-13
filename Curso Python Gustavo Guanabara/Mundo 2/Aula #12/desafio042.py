# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

# programa:
r1 = float(input('Comprimento da reta 1: '))
r2 = float(input('Comprimento da reta 2: '))
r3 = float(input('Comprimento da reta 3: '))

# descobrindo se forma triângulo:
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    if r1 == r2 == r3:
        print('Elas podem formar um triângulo \033[1;36mEquilátero\033[m.')
    elif r1 != r2 != r3 and r1 != r3:
        print('Elas podem formar um triângulo \033[1;31mEscaleno\033[m.')
    else:
        print('Elas podem formar um triângulo \033[1;33mIsósceles\033[m.')
else:
    print('\033[1;31mElas não podem formar um triângulo.')