# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'\033[1;33m{num} x {i:2} = {num*i}\033[m')