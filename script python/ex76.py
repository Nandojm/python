produto = ('Lapís',1.75 ,'Borracha', 2.00,'Caderno',15.90, 'Estojo', 25.00,'Transferidor',
            4.20,'Compasso', 9.99,'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
produtos = (('Lapís',1.75 ),('Borracha', 2.00),('Caderno',15.90), ('Estojo', 25.00),('Transferidor',
            4.20),('Compasso', 9.99),('Mochila', 120.32), ('Canetas', 22.30), ('Livro', 34.90))
css = '='*30
print(css)
print('{:^30}'.format('MEU JEITO INICIAL'))
print(css)
print(produto[0],'{:.>20}'.format('R$'),produto[1])
print(produto[2],'{:.>17}'.format('R$'),end=f'{produto[3]:>6.2f}\n')
print(produto[4],'{:.>18}'.format('R$'),end=f'{produto[5]:>6.2f}\n')
print(produto[6],'{:.>19}'.format('R$'),end=f'{produto[7]:>6.2f}\n')
print(produto[8],'{:.>13}'.format('R$'),end=f'{produto[9]:>6.2f}\n')
print(produto[10],'{:.>17}'.format('R$'),end=f'{produto[11]:>6.2f}\n')
print(produto[12],'{:.>18}'.format('R$'),end=f'{produto[13]:>6.2f}\n')
print(produto[14],'{:.>18}'.format('R$'),end=f'{produto[15]:>6.2f}\n')
print(produto[16],'{:.>20}'.format('R$'),end=f'{produto[17]:>6.2f}\n')

print(css)
print('{:^30}'.format('TUPLA COM PARES PRÉ DEFINIDOS'))
print(css)
for i, (nome, preco) in enumerate(produtos, start=1):
    print(f'{nome:.<20}R$  {preco:>6.2f}')

print(css)
print('{:^30}'.format('TUPLAS PLANA'))
print(css)
for i in range(0, len(produto), 2):
    nome = produto[i]
    preco = produto[i+1]
    print(f'{nome:.<20}R$  {preco:>6.2f}')

