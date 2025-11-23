print(' ')
print('--=' * 12)
print('{:^43}'.format('\033[35mOLHA A TABUADA \033[m'))
print('--=' * 12)
nu = int(input('Qual numero deja ver a tabuada ?'))    # busquei o numero que seria gerada a tabuada.
for c in range(1,11):                                  # fiz ser realizado a contagem de 1 até 10
    soma = c * nu                                      # somei o número (nu) vezes a quantidade (c)
    print('{} x {:2} = {}'.format(nu,c,soma))    # mostrei a tabuada de 1 até 10 com o resultado
print('--=' * 12)
print('{:^40}'.format('\033[35mFIM DA TABUADA \033[m'))
print('--=' * 12)
