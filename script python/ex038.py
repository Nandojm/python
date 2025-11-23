nu1 = int(input('Digite um numero inteiro: '))
nu2 = int(input('Digite outro numero: '))


if nu2 > nu1:
    print('O maior nunero foi {}'.format(nu2))
elif nu1 > nu2:
    print('O maior numero foi {}'.format(nu1))
else:
    print('O numero {} e o numero {} são iguais.'.format(nu1, nu2))