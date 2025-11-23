soma = 0
cont = 0
while True:
    try:
         numero = int(input('Digite um número [ 999 para parar ] '))
    except ValueError:
        print('Entrada inválida! Digite apenas números.')
        continue
    if numero == 999:
        break
    else:
        soma += numero
        cont +=1
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
