# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

# obtendo notas e calculando média:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

# analisando e respondendo:
if media < 5:
    print('\033[1;31mVocê foi reprovado!\033[m')
elif media > 5 and media < 6.9:
    print('\033[1;33mVocê está em recuperação.')
else:
    print('\033[1;32mVocê foi aprovado!')