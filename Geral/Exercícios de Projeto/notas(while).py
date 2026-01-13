notas = []

contador = 1

while contador <= 5:
    codigoAluno = int(input("RM: "))
    nota = float(input("Digite sua nota: "))
    resultado = [codigoAluno, nota]
    notas.append(resultado)

    # alternativa: contador += 1
    contador = contador + 1
    
print("Quantidade de notas: ", len(notas))