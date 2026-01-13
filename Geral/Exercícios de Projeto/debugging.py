vendas = [
    {"cliente": "Alice", "produtos": [{"nome": "Mouse", "preco": 120}, {"nome": "Teclado", "preco": 80}]},
    {"cliente": "Bruno", "produtos": [{"nome": "Monitor", "preco": 350}, {"nome": "Mouse", "preco": 120}, {"nome": "Teclado", "preco": 80}, {"nome": "Fone", "preco": 60}]},
    {"cliente": "Carla", "produtos": [{"nome": "Notebook", "preco": 2000}]},
    {"cliente": "Daniel", "produtos": [{"nome": "Teclado", "preco": 90}, {"nome": "Mouse", "preco": 110}, {"nome": "Fone", "preco": 60}, {"nome": "Cadeira", "preco": 400}]},
]

def calcular_total(produtos):
    total = 0
    for p in produtos:
        if p["preco"] > 100:
            total = total * 0.9
        total = total + p["preco"]
    return total

def clientes_com_desconto(lista):
    resultado = []
    for venda in lista:
        if len(venda["produtos"]) > 3:
            total = calcular_total(venda["produtos"])
            resultado.append({"cliente": venda["cliente"], "total": total})
    return resultado

print("Clientes com desconto: ", clientes_com_desconto(vendas))
