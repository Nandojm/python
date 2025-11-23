from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print("""Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA""")

jogador = int(input('Qual é a sua jogada ?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!')

print('-='*11)
print('Computador jogou {}.'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)

if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCE')
    elif jogador == 2:
        print('Computador VENCE')
    else:
        print('Jogada INVÁLIDA')
elif pc == 1:
    if jogador == 0:
        print('Computador VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('jogador VENCE')
    else:
        print('Jogada INVÁLIDA')
elif pc == 2:
    if jogador == 0:
        print('Jogador VENCE')
    elif jogador == 1:
        print('Computador VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')
