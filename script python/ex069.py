femenino = homens = maior_idade = 0
while True:
    print('--' * 20)
    print('CADASTRE UMA PESSOA')
    print('--' * 20)
    idade = int(input('Idade: '))
    if idade >= 18:
        maior_idade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ' )).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        femenino += 1
    if sexo == 'M':
        homens += 1
    continuar = ' '
    print('--' * 20)
    while continuar not in 'SN':
        continuar = str(input('Quer continuar ? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_idade} ')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {femenino} mulheres com menos de 20 anos')
