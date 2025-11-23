salario = float(input('Digite o salario: R$ '))

if salario > 1250:
    almento = salario + (salario * 10/100)
    print('O salário atual é de RS{:.2f}, mas com o novo aumento de 10% vai passar a ser de R${:.2f}'.format(salario, almento))
else:
    almento = salario + (salario * 15/100)
    print('Com o salário de R${:.2f} voce recebeu um aumento de 15%, co isso seu salário passa a ser de R${:.2f}'.format(salario, almento))