
#Obtendo dados:
print("Bem vindo(a)! Faça seu cadastro abaixo.")
usuario = input("Digite seu nome: ")
email = input("Digite seu email: ")
idade = (input("Digite sua idade: "))
while not idade.isdigit():
    idade = (input("Digite sua idade: "))
idade = int(idade)

#Analisando os dados:
if not idade > 0:
    print("Por favor, digite uma idade válida.")
elif email == "" or usuario == "":
    print("Por favor, preencha todos os campos.")

#Cadastrando
else:
    cadastrados = []
    cadastrados.append(usuario)
    cadastrados.append(email)
    cadastrados.append(idade)
    print("Cadastro concluido!")
    questao = input("Deseja ver a lista de cadastrados? (s/n): ")

#Finalizando programa:
if questao == "n":
    resposta = input("Deseja continuar o programa? (s/n): ").lower()
    if resposta == "n":
        print("Programa encerrado.")
        exit()
    elif resposta == "s":
        print("Programa continuado.")
    else:
        print("Por favor digite apenas 's' ou 'n'.")
        resposta = input("Deseja continuar o programa? (s/n): ").lower()
elif questao == "s":
    print(cadastrados)
else:
    print("Por favor digite 's' ou 'n'.")
