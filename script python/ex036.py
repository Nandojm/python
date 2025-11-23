print('--=--' * 10 )
color = { 'azul':'\033[7;34;034m',
          'limpa':'\033[m',
          'amarelo':'\033[33m',
          'verde':'\033[32m'}

print('                   {}Novo Banco{}'.format(color ['azul'], color ['limpa']))

print('--=--' * 10)
print('Empréstimo {}Imobiliária{}.'.format(color ['amarelo'], color ['limpa'] ))
print(' ' * 20)

valor = float(input('Digite o valor do imóvel: R$'))
salario = float(input('Qual é o valor do seu salario: R$'))
anos = int(input('Quer pagar em quantos anos? '))

meses = anos * 12
parcela = valor / meses
porcen =  (salario * 30 / 100)

print('     ' * 20)

if parcela <= porcen:
    print('{}PARABÉNS{}! Seu empréstimo foi aprovado.'.format(color ['verde'], color ['limpa']))
    print('Seu empréstimo de R${:.2f} foi aprovado em {} parcelas'.format(valor, meses))
    print(('Você vai pagar R${:.2f}  '.format(parcela)))
    print('  ')
elif parcela > porcen:
    print('Infelizmente seu empréstimo foi reprovado!')
    print('Seu salario de R${:.2f} não é suficiente para cobrir os 30% nescessario'.format(salario))
    print('Tente outra vez mais para frente.')
    print(' ')
print('Obrigado por escolher o {}Novo Banco{}'.format(color ['azul'], color ['limpa']))