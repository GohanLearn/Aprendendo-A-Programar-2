#Bellow, there  is a list example in Python:
lista = [1, 2, 3]
 #index: 0, 1, 2 (visual example)
print(lista[0])
print(lista[1])
print(lista[2])

#Every list have a thing called "Index".
#Index is the position of the list itens, and starts from "0".
#So, for get or print the first item from the list, we need to reffer to him like "0", not "1".

print("--------------------")
#We can change itens too.

lista_numeros = [1, 2, 3]

lista_numeros[0] = 5
print (lista_numeros[0])
print (lista_numeros[1])
print (lista_numeros[2])


print("--------------------")
#Lists can be different data, not only int.
numeros = [1, 2, 3]
strings = ["João", "Maria", "Bruxa"]
decimais = [10.8, 15.2, 33.3]

print("--------------------")
#We can include using appear.
lista_vazia = []

lista_vazia.append("Olá")
lista_vazia.append("Mundo!")

print(lista_vazia)

"""
Métodos para usar e praticar em listas explicados abaixo.
#
    append: Acrescenta um novo item no final da lista. (Mutador)
        lista_com_string.append("itemTeste")
        lista_com_inteiro.append(8)
        lista_com_decimal.append(4.9)
#
    insert: Insere um novo item na posição dada. (Mutador)
        lista.insert(1, "Banana")
#
    pop (Sem Parâmetro): Remove e retorna o ultimo item. (Hibrido)
        lista2.pop
    pop (Com Parâmetro): Remove e retorna o item da posição. (Hibrido)
        lista2.pop(3)
#
    sort: Ordena a lista, pode ordenar qualquer elemento comparável, exemplo: maior para menor, ordem alfabética. (Mutador)
        lista3.sort(reverse=False, Key=None)

#
    reverse: Ordena a lista em ordem reversa. (Mutador)
        lista4.reverse()
#
    index: Retorna a posição da primeira ocorrência do item.
        lista5.index(2)
#
    count: Retorna o número de ocorrências do item. (Retorna ct)
        lista6.count(2)
#
    remove: Remove a primeira ocorrência do item. (Mutador)
        lista7.remove("Banana")
    
    """