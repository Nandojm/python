nu = int(input('Digite um numero: '))
par = nu % 2
if par == 0:
    print('O numero {} é conciderado um numero par.'.format(nu))
else:
    print('O numero {} é conciderado um numero impar.'.format(nu))