lado1 = float(input('Digite o lado 1: '))
lado2 = float(input('Digite o lado 2: '))
lado3 = float(input('Digite o lado 3: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end= '')
    if lado1 == lado2 == lado3:
        print('EQUILÁTERO')
    elif lado1 != lado2 != lado3 != lado1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é possível formar um triângulo.')