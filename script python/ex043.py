print(' ')
print('--=--' * 10)
print(' ')

print('Tabela de IMC')
print(' ')
print('--=--' * 10)
print(' ')

altura = float(input('Qual é sua altura: '))
peso = float(input('Qual é o seu peso: '))

imc = peso / (altura **2)
ab = 18.5
ideal = 24.9
acima = 29.9
obe = 39.9
obm = 40

print(' ')

if imc < ab:
    print('Seu IMC é de {:.1f}. Você está abaixo do pesos, seu IMC ideal é de {}'.format(imc,ideal))
elif imc <= ideal:
    print('Seu IMC é de {:.1f}. Você está no seu peso ideal.'.format(imc))
elif imc < acima:
    print('Seu IMC é de {:.1f}. Você está com sobrepeso. Seu IMC ideal é de {}. CUIDE-SE!'.format(imc, ideal))
elif imc < obe:
    print('Seu IMC é de {:.1f}. Você precisa ir ao médico, você está obeso. O seu IMC ideal é {}.'.format(imc, ideal))
elif imc > obm:
    print('Seu IMC é de {:.1f}. Você sofre de obesidade mórbida, vá com urgência ao médico.'.format(imc))