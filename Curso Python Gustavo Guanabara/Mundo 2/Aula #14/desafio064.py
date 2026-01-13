# Crie um programa que leia varios números inteiros pelo teclado. O programa só para quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
total = 0
soma = 0
while True:
    val = int(input('Digite valores (999 para parar): '))
    if val == 999:
        print(f"""Quantidade de números digitados: {total} 
Resultado da soma entre eles: {soma}""")
        print('\033[1;31mPrograma encerrado.\033[m')
        break
    else:
        total += 1
        soma += val