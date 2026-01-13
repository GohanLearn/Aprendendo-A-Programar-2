# classes e funções
class Livro:
    def __init__(self, titulo, autor, ano, emprestado):
        self.titulo = titulo
        self.autor = autor
        self.ano = int(ano)
        self.emprestado = bool(emprestado)
    def __str__(self):
        if self.emprestado == False:
            emp = 'Não'
        else:
            emp = 'Sim'
        return f"Título: {self.titulo}\nAutor: {self.autor}\nAno de Lançamento: {self.ano}\nEmprestado: {emp}"

def emprestarLivro(livros, opcao):
    if livros[opcao].emprestado == False:
        livros[opcao].emprestado = True
        return print('Livro emprestado com sucesso!')
    else:
        return print('Livro não foi devolvido ainda.')

def devolverLivro(livros, opcao):
    if livros[opcao].emprestado == True:
        livros[opcao].emprestado = False
        return print('Livro devolvido com sucesso!')
    else:
        return print('Livro não foi emprestado ainda.')

# cadastro livros
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, False)
livro2 = Livro("1984", "George Owell", 1949, True)
livros = [livro1, livro2]
numLivros = len(livros)

print('\nLivros Cadastrados: ')
for i in range(0, numLivros):
    print(f'{i+1}. {livros[i].titulo}')
opcao = int(input('Escolha o número do livro: '))
print('1. Emprestar o livro\n2. Devolver o livro')
acao = int(input('Escolha a opção: '))

# agindo
if acao == 1:
    emprestarLivro(livros, opcao - 1)
elif acao == 2:
    devolverLivro(livros, opcao - 1)
else:
    print('\nLivro não existe!')