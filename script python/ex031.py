km = float(input('Informe a quantidade de Km rodado: '))
if km  <= 200:
    val = km * 0.50
    print('A distancia é de {}km com isso, o custo da passagem é de R${:.2f}'.format(km, val))
else:
    val2 = km * 0.45
    print('A distancia é de {:.3f}km, com isso, o custo da passagem é de R${:.2f}'.format(km, val2))

# preço = distancia * 0.50 is distancia <= 200 else distancia 0.45       isso é uma forma simplificada