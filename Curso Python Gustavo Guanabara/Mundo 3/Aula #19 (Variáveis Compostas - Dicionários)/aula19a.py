# Nessa aula, aprendemos sobre dicionários (dicts).
# Na hora de declarar, é bom se usar ASPAS SIMPLES, já na hora de usar usar ASPAS DUPLAS. Exemplo:
# dicio = {'nome':'STAR'} # print(dicio["nome"])
dict = {
    'nome':'Star Wars',
    'ano':1977,
    'autor':'George'
}
# keys = nome, ano, autor
# values = Star Wars, 1977, George
# items = nome, Star Wars, ano, 1977, autor, George
print(dict['nome'])
# del
for k, v in dict.items():
    print(f'{k} = {v}')
# dicionarios nao podem usar [:], mas podem usar .copy()