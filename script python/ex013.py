salario = float(input('Qual é o seu salário? R$'))
novo = salario + (salario * 15 / 100)
#novo = salario * 1.15
print('O seu salário é de R${:.2f}, mas com o seu almento '
      'de 15%, seu salario passa a ser de R${:.2f} '.format(salario, novo))