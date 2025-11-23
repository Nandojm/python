print('SOMA DE PRODUTOS!  [SAIR/S] PARA PARAR.')
lista = []
tupla = ('S', 'N')
soma = contador = preco = 0
while True:
    produto = str(input('Qual é o produto: ')).strip().upper()

    try:
        preco = float(input('Digite o valor R$'))
    except ValueError:
        continue
    try:
        quantidade = int(input('Quantos produtos?'))
    except ValueError:
        continue
    contador += 1
    lista.append(produto.capitalize())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
        if continuar in tupla:
            break
        print('[ERRO] Tente novamente.')
    preco *= quantidade
    soma += preco
    if continuar == 'N':
        break
    print('-' * 25)
if contador == 1:
    print(f'Você comprou {contador} produto, que foi:')
elif contador >1:
    print(f'Você comprou {contador} produtos, que foram:')
print(', '.join(lista))
print(f'Com o total de R${soma:.2f}')