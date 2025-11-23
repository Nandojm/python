din = float(input('Digite quanto você tem de dinheiro: R$'))
cot = float(input('Qual é a cotação da moeda? '))
dolar = din / cot
print('Com a quantia de R${:.2f}, você consegue comprar US${:.2f} '.format(din, dolar,))
