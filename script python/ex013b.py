sal = float(input('Qual é o valor do salario do funcionario? R$'))
aum = float(input('Agora quantos porcento você quer dar de almento:'))
novo = sal + (sal * aum / 100)
print('O salario do funcionario era de {:.2f}, mas com o novo almento de {:.2f}%,'
      ' passa a ser de R${:.2f}'.format(sal, aum,novo))
print('Agora tendo em vista o novo almento de {}%, '
      'sua diaria que antes era de R${:.2f} passa a ser de R${:.2f}'. format(aum, sal/22, novo/22))