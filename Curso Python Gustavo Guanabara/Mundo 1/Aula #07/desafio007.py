# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

# obtendo notas
nota1 = float(input('\033[1;32mPrimeira nota do aluno: '))
nota2 = float(input('\033[1;32mSegunda nota do aluno: '))

# calculando
media = (nota1 + nota2) / 2

# mostrando
print('\033[1;33mA média entre {} e {} é igual a {:.1f}'.format(nota1, nota2, media))