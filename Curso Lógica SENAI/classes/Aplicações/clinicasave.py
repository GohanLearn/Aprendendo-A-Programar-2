# classe para guardar dados do paciente
class Paciente:
    pacientes = []
    max = 3
    contador = 0
    def __str__(self):
        return ('-'*20, f'Paciente {Paciente.contador}\nNome: {Paciente.nome}\nIdade: {Paciente.idade}\nProcedimento: {Paciente.procedimento}\nValor do Procedimento: {Paciente.valorProc}', '-'*20)
    def __init__(self, nome, idade, procedimento, valorProc):
        if Paciente.contador < Paciente.max:
            self.nome = nome
            self.idade = int(idade)
            self.procedimento = procedimento
            self.valorProc = float(valorProc)
            Paciente.contador += 1
            Paciente.pacientes.append(self)
        else:
            print('Máximo de pacientes alcançado.')
            print(input('Pressione ENTER para visualizar a lista de pacientes.'))
            print('\n ** Relatório de Pacientes e Procedimentos da Clínica **')
            for i in range(0, Paciente.contador):
                print(Paciente.pacientes[i])

# programa principal
print('Clínica Osso Leite Azul')
while Paciente.contador < Paciente.max:
    nomeP = input('Nome do paciente: ')
    idadeP = int(input('Informe a idade: '))
    procedP = input('Informe o procedimento: ')
    valorProcedP = float(input('Informe o valor do procedimento: '))
    Paciente(nomeP, idadeP, procedP, valorProcedP)
    continuar = input('Deseja cadastrar mais um paciente? (s/n): ')
    if continuar == 's' or continuar == 'S':
        if Paciente.contador < Paciente.max:
            continue
        else:
            print('Máximo de pacientes alcançado.')
            print(input('Pressione ENTER para visualizar a lista de pacientes.'))
            print('\n ** Relatório de Pacientes e Procedimentos da Clínica **')
            for i in range(0, Paciente.contador):
                print(Paciente.pacientes[i])
    else:
        print(input('Pressione ENTER para visualizar a lista de pacientes.'))
        print('\n ** Relatório de Pacientes e Procedimentos da Clínica **')
        for i in range(0, Paciente.contador):
            print(Paciente.pacientes[i])