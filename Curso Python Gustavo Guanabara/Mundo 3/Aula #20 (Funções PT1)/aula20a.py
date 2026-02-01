# Nessa aula, aprendemos sobre funções.
def soma(a, b):
    s = a + b
    print(s)


# programa principal
soma(float(input('Primeiro Valor: ')), float(input('Segundo Valor: ')))



# para uma função receber valores indefinidamente, python nos permite empacotar:
def contador(* num): # adicione um asterisco na frente de uma variavel que vai receber varios valores
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


# usando funções em listas
print('\n')
def dobrar(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [2, 4, 7, 8]
dobrar(valores)
print(valores)