while True:
    nu = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 15)
    if nu < 0:
        break
    for c in range(1, 11):
        print(f'{nu} x {c} = {nu*c}')
    print('--' * 15)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')