# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

# programa:
lista = []
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if len(lista) > 0:
        for v in lista:
            if valor < v:
                lista.insert(lista.index(v), valor)
                print(f'Valor adicionado na posição {lista.index(v)-1}.')
                break
            if valor > max(lista):
                lista.append(valor)
                print('Valor adicionado ao final da lista.')
                break
    else:
        lista.append(valor)
        print('Valor adicionado ao final da lista.')
print(f'Os valores digitados em ordem foram {lista}')