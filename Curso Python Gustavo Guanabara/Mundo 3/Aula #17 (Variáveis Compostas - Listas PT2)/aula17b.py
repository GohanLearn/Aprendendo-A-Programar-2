# Nessa aula, aprendemos sobre listas compostas (Listas dentro de Listas).
pessoas = [['Maria', 25], ['Pedro', 18], ['Antônio', 57]]
print(pessoas[0][1])
for p in pessoas:
    print(f'{p[0]} tem {p[1]} anos')
print('\n')

# criando lista
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

# testes extras
print('\n')
galerona = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galerona.append(dado[:]) # se esquecer o [:], as listas ficam em ligação e o print vai ser afetado pelo clear.
    dado.clear()
print(galerona) # [:] = cria uma cópia de dado, não uma ligação.