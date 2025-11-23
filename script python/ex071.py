print('=' * 30)
print('{:^30}'.format('NOVO BANCO'))
print('=' * 30)
saque = int(input('Que valor você quer sacar? R$'))
total = saque
ced = 50
quant = 0
while True:
    if total >= ced:
        total -= ced
        quant += 1
    else:
        print(f'Total de {quant} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        quant = 0
        if total == 0:
            break
print('Obrigado por escolher o NOVO BANCO!')