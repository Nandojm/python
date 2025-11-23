par = 0
cont = 0
for c in range(1,7):
    nu = int(input('Digite o numero: '))
    if nu % 2 == 0:
        par += nu
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}'.format(cont,par))