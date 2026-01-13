# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

# recebendo número
num = int(input('\033[1;35mDigite um número inteiro para converter: \033[m'))

# escolhendo conversão
print('-=-'*20)
print('\033[1;33mConversões:\033[m')
print('1 - Binária\n2 - Octal\n3 - Hexadecimal')
print('-=-'*20)
tipo = int(input('Digite qual conversão você quer: '))

# respondendo
if tipo == 1:
    print(bin(num))
elif tipo == 2:
    print(oct(num))
elif tipo == 3:
    print(hex(num))
else:
    print('Opção inválida.')