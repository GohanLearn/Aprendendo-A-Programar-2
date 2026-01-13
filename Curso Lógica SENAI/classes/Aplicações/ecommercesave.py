# classes
class Produto:
    produtosDisp = [
        {"Nome": "Camiseta Branca", "Preço": 29.99},
        {"Nome": "Calça Jeans", "Preço": 199.99},
        {"Nome": "Tênis", "Preço": 99.99},
    ]
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)


# programa principal
carrinho = []
contador = 1
print('-'*25)
print('Produtos Disponíveis:')
for produto in Produto.produtosDisp:
    print(f"{produto['Nome']} - R${produto['Preço']}")
while contador == 1:
    escolha = input('Escolha um produto para adicionar no carrinho (0 para sair): ')
    if escolha == '0':
        break
    elif escolha == '1':
        carrinho.append(Produto.produtosDisp['Nome', 'Preço'])
    elif escolha == '2':
        carrinho.append(Produto
                        


    if escolha == 0:
        break
    elif escolha == 1:
        carrinho.append(Produto.produtosDisp['Nome', 'Preço'])
    elif escolha == 2:
        carrinho.append(Produto.produtosDisp[escolha])