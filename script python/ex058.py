from random import randint
from time import sleep

computador = randint(0,10)
print('--' * 20)
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")
palpite = 0 # coloquei estas 2 variáveis aqui em cima para poder colocar elas no FORMAT quando for preciso
contador = 0
print(' ')

while palpite != computador: # enquanto o palpite do jogador for diferente do número que o computador escolheu, ele vai dar a dica se é mais ou menos e vai manda tenta de novo.
    palpite = int(input('Qual é o seu palpite? '))
    contador +=1 # vai contar quantas vezes o jogador tentou.
    print(' ')
    print('\033[31mANALISANDO...\033[m')
    print(' ')
    sleep(2)# esse sleep vai fazer esperar por 2 segundos
    if palpite != computador: # vai mostrar a mensagem de erro se o jogador errar
        if palpite < computador: # se ele tiver jogado um número baixo de mais, vai mandar jogar mais alto
           print('Mais... Tente mais uma vez.')
        else: # se tiver jogado alto de mais, vai mandar jogar menos
            print('Menos...Tente mais uma vez.')
    else:# quando ele acerta vai mandar a mensagem que acertou e vai mostrar quantas tentativas foram feitas.
        print('Você acertou na {}º tentativa.\033[32m PARABÉNS\033[m!'.format(contador))
