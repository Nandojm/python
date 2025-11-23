from math import ceil
no1 = float(input('Digite a primeira nota do aluno: '))
no2 = float(input('Digite a segunda nota do aluno: '))


media = (no1 + no2) /2
if media >= 7:
    print('PARABÉNS! Sua media é {:.1f} você passou de ano.'.format(media))
elif media >= 5:
    print('Você ficou de recuperação! Suamedia é {:.1f} estude mais.'.format(media))
elif media < 5:
    print('Sua média é {:.1f}. Você foi REPROVADO.'.format(media))

