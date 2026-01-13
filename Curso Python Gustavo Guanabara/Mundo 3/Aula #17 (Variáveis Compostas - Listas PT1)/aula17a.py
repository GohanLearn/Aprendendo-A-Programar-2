# Na Aula 17, prendemos sobre listas e alguns comandos simples, exemplos:
lista = [2, 1, 3, 4, 7]
lista.append(9) # adiciona '9' a lista
lista.sort() # organiza a lista em ordem crescente
lista.sort(reverse=True) # organiza a lista em ordem decrescente
lista.insert(2, 0) # insere '0' na posição 2
lista.pop() # remove o ultimo elemento da lista
lista.pop(2) # remove o elemento da posição 2
if 4 in lista:
    lista.remove(4) # remove a primeira ocorrência do valor 2
else:
    print('Não encontrei.')
print(lista)
for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('\n'*7)
# Peculiaridade do Python:
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# No momento em que igualamos uma lista a outra, o Python cria uma ligação entre elas. Para evitar essa ligação, fazemos:
print('\n'*3)
a2 = [2, 3, 4, 7]
b2 = a2[:]
b2[2] = 8
print(f'Lista A: {a2}')
print(f'Lista B: {b2}')