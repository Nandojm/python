n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
for c  in range (n, 0,-1):
    print ('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
print(f'{f}')