print('{: ^40}'. format('CASAS BAHIAS'))
soma = contador = 0
mais_barato = None
produto_mais_barato = ''
while True:
    print('--' * 20)
    produto = str(input('Nome do produto: '))
    try:
        preco = float(input('Qual é o preço? R$'))
    except ValueError:
        continue
    soma += preco
    if preco >= 1000:
        contador += 1
    if (mais_barato is None) or (preco < mais_barato): # usar mais o none e estudar mais a sequecia de validar valores
        mais_barato = preco
        produto_mais_barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('--' * 20)
print(f'O total gasto foi R${soma:.2f}')
print(f'Foram comprados {contador} produtos com preço superior a R$1000.00')
print(f'O produto mais barato que foi {produto_mais_barato} custou R${mais_barato:.2f} ')