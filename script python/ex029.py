vel = int(input('Qual é a velocidade atua? '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você ultrapassou a velocidade permitida de 80 km/h.')
    print('Você foi multado em R${:.2f}'.format(multa))
print('Muito bem! Dirigija com segurança.')
