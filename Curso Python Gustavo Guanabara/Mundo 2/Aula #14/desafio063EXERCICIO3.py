n = int(input('Digite quantos termos você quer: '))
t1 = 0 # a sequência sempre começa com 0
t2 = 1 # o segundo termo sempre é 1
cont = 3
print(f'{t1} -> {t2} -> ', end = '') # mostra os dois primeiros termos
while cont <= n:
    t3 = t1 + t2 # o termo mostrado é a soma dos dois termos anteriores
    print(f'{t3}', end = ' -> ')
    t1 = t2 # t1 se torna t2
    t2 = t3 # t2 se torna t3
    cont += 1
    # o ciclo se repete até o fim
print('FIM')