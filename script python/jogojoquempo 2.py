from random import choice
print(' ')
print('                \033[35m Joquempô \033[m     ')
print(' ')
print('\033[33m--=--\033[m' * 10 )

jogador1 = str(input('Jogador \033[33m nº1 \033[m. Você escolhe primeiro: '))
jogador2 = str(input('Jogador \033[36m nº2 \033[m. Agora é sua vez: '))

print('\033[33m--=--\033[m' * 10)

jogo = ["pedra", "papel", "tesoura"]
computador = choice(jogo)
if computador == 'pedra' and jogador1 == 'pedra':
    print('Parabéns jogador \033[33m nº1 \033[m você ganhou!')
elif computador == 'pedra' and jogador2 == 'pedra':
    print('Jogador \033[36m nº2 \033[m você ganho!')
elif computador == 'papel' and jogador1 == 'papel':
    print('Jogador \033[33m nº1 \033[m você ganhou!')
elif computador == 'papel' and jogador2 == 'papel':
    print('Jogador \033[36m nº2 \033[m você ganhou!')
elif computador == 'tesoura' and jogador1 == 'tesoura':
    print('Jogador \033[33m nº1 \033[m você ganhou!')
elif computador == 'tesoura' and jogador2 == 'tesoura':
    print('Jogador \033[36m nº2 \033[m você ganhou!')
elif jogador1 == jogador2:
    print('Vocês empataram')
    #print('Infelizmente vocês perderam, eu escolhi \033[31m{}\033[m, então eu ganhei!.'.format(computador))
