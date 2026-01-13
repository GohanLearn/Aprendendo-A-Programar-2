# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*30)
    for i in range(1, 11):
        print(f'{num} x {i:2} = {num*i}')
    print('-'*30)
print('\033[1;31mPrograma encerrado.\033[m')