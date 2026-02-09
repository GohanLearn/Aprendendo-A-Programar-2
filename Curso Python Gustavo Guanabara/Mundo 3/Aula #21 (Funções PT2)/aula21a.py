# Nessa aula, aprendemos sobre help(), docstrings, return, escopos (globais e locais) e etc.

def fatorial(num=1):
    f = 1
    for c in range(num, f, -1):
        f *= c
    return f

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)} ')
if par(n):
    print('É par!')
else:
    print('Não é par!')