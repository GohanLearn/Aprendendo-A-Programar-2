# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

# bibliotecas:
from time import sleep

# funções:
def contador(início, fim, passo):
    print('-=-'*10)
    if passo < 0:
        passo = -passo
    elif passo == 0:
        passo = 1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if início > fim:
        while início >= fim:
            sleep(0.3)
            print(início, end = ' ', flush = True)
            início -= passo
    else:
        while início <= fim:
            sleep(0.3)
            print(início, end = ' ', flush = True)
            início += passo
    print('FIM')
    print('-=-'*10)


# programa principal:
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)