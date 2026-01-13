# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaAlunos)
print('A ordem escolhida foi: ')
print(listaAlunos)



#for i in range(0, 4):
#    escolhido = random.choice(listaAlunos)
#    listaSorteada.append(escolhido)
#    listaAlunos.remove(escolhido)