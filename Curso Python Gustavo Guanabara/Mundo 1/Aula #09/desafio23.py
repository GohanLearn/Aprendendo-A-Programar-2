# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

# programa:
num = input("Digite um número: ")
tamanho = int(len(num))
print(f"unidade: {num[tamanho-1]}")
print(f"dezena: {num[tamanho-2]}")
print(f"centena: {num[tamanho-3]}")
print(f"milhar: {num[tamanho-4]}")



# tamanho = int(len(num))
# print(f"unidade: {num[tamanho-1]}")
# if tamanho > 1:
#    print(f"dezena: {num[tamanho-2]}")
#    if tamanho > 2:
#        print(f"centena: {num[tamanho-3]}")
#        if tamanho > 3:
#            print(f"milhar: {num[tamanho-4]}")