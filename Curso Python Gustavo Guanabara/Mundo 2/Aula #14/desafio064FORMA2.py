# Crie um programa que leia varios números inteiros pelo teclado. O programa só para quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
num = cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
#    if num == 999:
#        soma -= 999
#        cont -= 1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')