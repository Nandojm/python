from selectors import SelectSelector
from time import sleep

print('--=--' * 10 )
cores = {'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde':'\033[32m',
         'limpa':'\033[m'}

print('Ola, Eu sou a Bia! Seja bem vindo a {}Holywood{}! '.format(cores ['amarelo'], cores['limpa']))
sleep(3)
print(' ' * 20)
nome = str(input('Qual é o seu nome?')).capitalize().strip()
print(' ' * 20)

print('É um prazer te conhecer {}{}{}.'.format(cores['verde'],nome, cores ['limpa']))
sleep(2)
sexo = str(input('Agora gostario de saber, se você é uma menina ou um menino ? '))

print(' ' * 20)

if sexo == 'menino':
    print('Então você está pronto para ter sucesso e fama aqui em holywood irmão?')
    sim = str(input('Sim ou Nao ?\n')).capitalize().strip()
    if sim == 'Sim':
        print('historia em desenvolvimento.')
else:
    print('Então você está pronta para fazer muito sucesso em Hollywood e ser uma POP STAR ?')
    sim = str(input('Sim ou Nao ?')).capitalize().strip()
    if sim == 'Sim':
        print('Para se ter sucesso aqui você precisa se esforçar. ')
        print('Vamos começar sabendo qual é a carreira que você quer aqui em hollywood.')
        prof = str(input('O que você quer fazer em hollywood, ser uma cantora ? ou uma atriz de filmes ? \nOu talves uma dançarina ou até mesmo quer viver nas ruas? voce que me diz.  ')).capitalize().strip()

        if prof == 'Cantora':
            print("""Então para ser uma cantora de sucesso, você precisa começar a fazer uma aula de canto
Ou vocÊ pode começar a cantar em bares da região.""")
            din = float(input('Quanto de dinheiro você trousse para começar sua nova vida ? '))
            if din < 100000:
                print('Nossa você conseguiu trazer tudo isso? mas infelismente isso ainda nãe é suficiente para bancar seu estudos')

        else:
            if prof == 'Dançarina':
                print("""Então para ser uma dançarina de sucesso, você precisa entrar em uma aula de dança
Ou vocÊ pode começar a dançar em bares da região, mas acho que isso não é uma boa ideia""")
                din = float(input('Quanto de dinheiro você trousse para começar sua nova vida aqui ? R$ '))
                if din < 100000:
                    print('Nossa você conseguiu trazer tudo isso? mas infelismente isso ainda nãe é suficiente para bancar seu estudos')
            else:
                if prof == 'Atriz':
                    print('Então para ser uma Atriz de sucesso, você precisa começar a fazer uma aula de teatro \nOu vocÊ pode começar a dançar em bares da região, mas acho que isso não é uma boa ideia ')
                    din = float(input('Quanto de dinheiro você trousse para começar sua nova vida aqui ? R$'))
                    print('Nossa você conseguiu trazer tudo isso? mas infelismente isso ainda nãe é suficiente para bancar seu estudos')




