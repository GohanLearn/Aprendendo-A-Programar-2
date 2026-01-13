# Variáveis Compostas ( Tuplas )
# () = tupla
# [] = lista
# {} = dicionário
lanche = ('hamburguer', 'suco', 'pizza', 'pudim') # a partir do python 3.5, não precisa mais de parênteses
# Tuplas são IMUTÁVEIS
print(lanche)
print(lanche[2])
print(lanche[0:2])
print(lanche[1:])
print(lanche[-1])
print(len(lanche))
for c in lanche:
    print(c)
print(lanche[1:3])
print(sorted(lanche))
del(lanche)