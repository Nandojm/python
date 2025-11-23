brasileirao = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia',
               'Botafogo', 'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá',
               'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional',
               'Juventude', 'Palmeiras', 'Red Bull Bragantino', 'Santos',
               'São Paulo', 'Vasco da Gama', 'Vitória')
css = ('=-' * 15)
print(f'Lista de times do Brasileirão: {brasileirao}')
print(css)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print(css)
print(f'Os 4 últimos são {brasileirao[-4:]}')
print(css)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print(css)
time = brasileirao[11]
print(f'O {time} está na {brasileirao.index(time)+1}ª posição.')