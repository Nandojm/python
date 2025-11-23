from random import randint
from time import sleep
print('-=-' * 15) # bota linhas no programa
nu = randint (0,5)
print('Vou pensar em um numero de 0 a 5')
print('-=-' * 15)
sorte = int(input('Digite um numero de 0 a 5: '))

print(' ' * 25)

print('ANALISANDO...')

print('  '* 25)

sleep(3)
if sorte == nu:
    print('Parabéns! você acertou!')
else:
    print('Você errou, o numero que escolhi foi {}, tente novamente!.'.format(nu,))
