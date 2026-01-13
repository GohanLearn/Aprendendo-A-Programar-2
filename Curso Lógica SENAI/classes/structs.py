# imports
import os

# definição da classe Aluno
class Aluno:
    def __init__(self, nome, idade, matricula, notas):
        self.nome = nome
        self.idade = int(idade)
        self.matricula = int(matricula)
        self.notas = notas
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nMatrícula: {self.matricula}\nNotas: {self.notas}'

# definindo listas
alunosLista = []

# obtendo dados
alunos = int(input('Digite a quantidade de alunos: '))
notasQuantidade = int(input('Digite a quantidade de notas: '))
for i in range(alunos):
    os.system('cls')
    print(f'\nAluno {i + 1}')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    matricula = int(input('Matrícula: '))
    notasLista = []
    for j in range(notasQuantidade):
        notaVar = float(input(f'Nota {j + 1}: '))
        notasLista.append(notaVar)
    alunosLista.append(Aluno(nome, idade, matricula, notasLista))
    os.system('cls')
for aluno in alunosLista:
    print('\n', aluno)