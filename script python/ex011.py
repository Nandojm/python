alt = float(input('Qual é a altura da parede? '))
larg = float(input('Agora me diga a largura: '))
mq = alt * larg
tin = mq / 2
print('A área da sua parede tem {:.3f}m metros quadrados. Sabendo isso, você vai '
      'precisar de {:.3f} litros de tinta.'.format(mq,tin))
