# definindo a classe para moldar pacientes e seus atributos
class Paciente:
    pacientes = []
    totalPacientes = 0
    def __str__(self):
        return f'Paciente {self.numero}\nNome: {self.nome}\nIdade: {self.idade}\nQuarto: {self.quarto}\n'
    def __init__(self, numero, nome, idade, quarto):
        self.numero = int(numero)
        self.nome = nome
        self.idade = int(idade)
        self.quarto = int(quarto)
        Paciente.pacientes.append(self)
        Paciente.totalPacientes += 1


# programa principal // obtendo dados dos pacientes
numeroP = 0
print('Registro de pacientes no Hospital Arterial')
while True:
    pacienteN = input('Nome do Paciente: ')
    pacienteI = int(input('Idade do Paciente: '))
    pacienteQ = int(input('Qual o quarto? '))
    numeroP += 1
    Paciente(numeroP, pacienteN, pacienteI, pacienteQ)
    continuar = input('Você deseja registrar mais um paciente? (s/n): ')
    if continuar == 'n' or continuar == 'N':
        print('\n')
        for i in range(0, Paciente.totalPacientes):
            print(Paciente.pacientes[i])
        break
    else:
        if Paciente.totalPacientes < 5:
            print('\n')
            continue
        else:
            print('Quantia máxima de pacientes alcançada.')
            input('Pressione ENTER para mostrar a lista de pacientes. ')
            print('\n')
            for i in range(0, Paciente.totalPacientes):
                print(Paciente.pacientes[i])