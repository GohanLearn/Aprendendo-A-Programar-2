    # idade
# obtendo informação
idade = int(input("Digite sua idade: "))

# checando
if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade")


    # loop
numeros = 0

for numeros in range (1, 11):
    print(numeros)


    # lista
lista1 = [1, 2, 3, 4, 5]
print(lista1)
print(min(lista1))
print(max(lista1))


    # dicionario
pessoa = {
    "Nome": '...',
    "Idade": '...'
}
print("Nome:", pessoa['Nome'])
print("Idade:", pessoa['Idade'])


    # função
def somar(valor1, valor2, valor3):
    return valor1 + valor2 + valor3
while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    valor3 = int(input("Valor3: "))

    resposta = somar(valor1, valor2, valor3)
    media = float(valor1 + valor2 + valor3) / 3
    print(valor1, "+", valor2,"+", valor3, "=", resposta)
    print(valor1, "+", valor2,"+", valor3, "/ 3 =", media)
    break