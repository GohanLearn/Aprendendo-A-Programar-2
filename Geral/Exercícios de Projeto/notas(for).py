notas = []
for x in range(5):
    codigoAluno = int(input("RM: "))
    nota = float(input("Digite sua nota: "))
    resultado = [codigoAluno, nota]
    notas.append(resultado)


print("Quantidade de notas: ", len(notas))

for n in notas:
    codigoAluno = n[0]
    nota = n[1]
    print("O RM", codigoAluno, "tirou a nota:", nota)