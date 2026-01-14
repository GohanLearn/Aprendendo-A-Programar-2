# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

# programa:
lista = []
escolha = 'S'
while escolha in 'Ss':
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print(f'O valor {valor} já existe na lista e não foi adicionado.')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
    while not escolha in 'SsNn':
        escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
print('Os valores digitados em ordem crescente foram: ', end = '')
print(sorted(lista))