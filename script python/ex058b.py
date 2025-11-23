from random import randint # importei da biblioteca random o randint
computador = randint(0,10) # computador gera um número de 0 a 10
print("""Sou o seu computador...
Acabei de pensar em um numero de 0 a 10.
Será que você consegue adivinhar qual foi?""")
acertou = False # variavel acertou como falsa
palpite = 0 # contador com 0
while not acertou: # em quanto não acerta vai continuar se repetindo
    jogador = int(input('Qual é seu palpite? ')) # jogador vai dar o seu palpite
    palpite += 1 # sempre que o jogador der um palpite, vai contar
    if jogador == computador: # a parte importante: se o palpite do jogador for igual ao computador
        acertou = True # acertou vai se tornar verdadeiro e vai para o último print que fala que acertou
    if jogador < computador:# agora se jogador de um palpite menor que o número do computador
        print('Mais... Tente mais uma vez.') # aparece esta mensagem
    elif jogador > computador: # se o palpite for maior do que o número do computador
        print('Menos... Tente mais uma vez.')# mostra esta mensagem

print('Você acertou na {}º tentativa. \033[32mPARABÉNS\033[m!'.format(palpite)) # aqui so vai aparecer quando o ACERTOU for verdadeiro