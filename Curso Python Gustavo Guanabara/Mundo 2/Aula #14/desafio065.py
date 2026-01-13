# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
total = 0
quantidade = 0
media = 0
maior = 0
menor = 0
while True:
    num = int(input('Digite um número inteiro: '))
    escolha = str(input('Quer continuar a digitar números? [S/N]: ')).upper().strip()
    if escolha == 'N':
        media = total / quantidade
        print(f"""Média: {media}
Maior: {maior}
Menor: {menor}""")
        print('\033[1;31mPrograma encerrado.\033[m')
        break
    else:
        quantidade += 1
        total += num
        if num > maior:
            maior = num
        if num < menor or menor == 0:
            menor = num
        continue