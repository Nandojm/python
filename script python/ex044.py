print(' ')
print('--=--'*10)
print('{:^45}'.format('LOJA GUANABARA'))
print('--=--'*10)
print(' ')

preco = float(input('Qual é o valor do produto? R$'))
print("""FORMA DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão""")
pagamento = int(input('Qual é a opção ? '))

avista = preco - ( preco * 10/100 )
ac = preco - (preco * 5/100)
x3 = preco + (preco * 20/100)
if pagamento == 4:
    parcela = int(input('Quantas parcelas ?'))
    valor = x3 / parcela
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela, valor))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, x3))
elif pagamento == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, ac))
elif pagamento == 3:
    valor = preco / 2
    print('Sua compra sera parcelada em 2x de R${:.2f} SEM JUROS.'.format( valor))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, preco))
elif pagamento == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, avista))
else:
    parcela = 0
    print('OOPÇÃO INVALIDA de pagamento. Tente novamente!')