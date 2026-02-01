# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer quais deles é o maior.

# funções:
def maior(* valores):
    m = 0
    print('-=-'*10)
    print('Analisando valores informados...')
    for v in valores:
        print(v, end=' ')
        if v > m:
            m = v
    print(f' Foram ao todo {len(valores)} informados.')
    print(f'O maior valor foi {m}')
    print('-=-'*30)


# programa principal:
maior(2, 9, 4, 5, 7, 1)
maior()