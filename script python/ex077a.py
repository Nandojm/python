lista = ('arroz','cachorro','carro','Borboleta','celular',
            'bicicleta', 'papagaio', 'estrela', 'lua', 'computador',
            'caixa','jumento', 'aviao')
vogais = 'aeiou'
for palavra in range(0, len(lista)):
    objeto = lista[palavra]
    voga = ' '
    for i in objeto:
        if i in vogais:
            voga += i + ' '
    print(f'Na palavra {objeto.upper()} temos as vogais: {voga}')