contador = soma = 0
while True:
    nu = int(input('Digite um número (999 faz parar): '))
    if nu == 999:
        break
    soma += nu
    contador += 1
print(f'Você digitou {contador} e a soma foi {soma}')
