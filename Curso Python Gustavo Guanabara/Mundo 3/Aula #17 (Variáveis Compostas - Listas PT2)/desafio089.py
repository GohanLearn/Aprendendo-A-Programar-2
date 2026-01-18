# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

### Suporte: alunos = [[[]]]

# programa
alunos = list()
boletim = list()
notas = list()

while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    media = round(media, 1)
    boletim.append(nome)
    notas.append(nota1)
    notas.append(nota2)
    boletim.append(notas[:])
    boletim.append(media)
    alunos.append(boletim[:])
    boletim.clear()
    notas.clear()
    escolha = str(input('Quer continuar? [S/N] ')).strip()[0]
    if escolha in 'Nn':
        break
print('-=-'*15)
print(f'{"No.":<4}{"NOME":<15}{"MÉDIA":>6}')
print('-'*30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<15}{a[2]:>6}')
print('-'*30)

# parte de demostração dos boletins
while True:
    demostra = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if demostra == 999:
        break
    print(f'Notas de {alunos[demostra][0]} são {alunos[demostra][1]}')
    print('-'*30)
print('\033[1;31mPrograma finalizado.\033[m')