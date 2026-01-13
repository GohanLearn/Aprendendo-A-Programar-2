# classes
class Produto:
    produtosDisp = [
        {"nome": "Camiseta Branca", "preco": 29.99},
        {"nome": "Calça Jeans", "preco": 199.99},
        {"nome": "Tênis", "preco": 99.99}
    ]
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)


# programa principal
carrinho = []
contador = 1
print('-'*25)
print('Produtos Disponíveis:')
for i, produto in enumerate(Produto.produtosDisp, start=1):
    print(f'{i}. {produto["nome"]} - R$ {produto["preco"]}')
while contador == 1:
    escolha = int(input('Escolha um produto para adicionar no carrinho (0 para sair): '))
    if escolha == 0:
        valorT = sum(produto["preco"] for produto in carrinho)
        print(f'\nTotal da Compra: R$ {valorT}')
        break
    carrinho.append(Produto.produtosDisp[escolha-1])



# "Camiseta Branca - R$ 29.99", "Calça Jeans - R$ 199.99", "Tênis - R$ 99.99"