# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
tabela = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print(f'Os ultimos 4 colocados são: {tabela[-4:]}')
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'O time da Chapecoense está na {tabela.index('Chapecoense')+1}ª posição')