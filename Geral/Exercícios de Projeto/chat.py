import os

mensagens = []

nome = input("Nome: ")

while True:

    # limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________")

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break
    while len(texto) > 100:
        print("Texto grande demais.")
        texto = input("mensagem: ")
        break
    # adicionando mensagem na lista
    mensagens.append ({
        "nome": nome,
        "texto": texto
    })