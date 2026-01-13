# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
PrimeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termos = 0
quantia = 10
while termos < quantia:
    print(PrimeiroTermo, end = ' -> ')
    PrimeiroTermo += razao
    quantia -= 1
print('Final')
while True:
    escolha = int(input('Quer mais termos? Quantos? '))
    if escolha != 0:
        quantia = escolha
        termos = 0
        while termos < quantia:
            PrimeiroTermo += razao
            print(PrimeiroTermo, end = ' -> ')
            termos += 1
        print('PAUSA')