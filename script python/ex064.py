soma = 0
cont = 0
sair = False

while not sair:
    numero = int(input('Digite um número [ 999 para parar ] '))
    if numero != 999:
        soma += numero
        cont += 1
    elif numero == 999:
        sair = True

print(f'Você digitou {cont} números e a soma entre eles foi {soma}')