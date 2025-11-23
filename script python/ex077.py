palavras = ('arroz','cachorro','carro','Borboleta','celular',
            'bicicleta', 'papagaio', 'estrela', 'lua', 'computador',
            'caixa','jumento', 'aviao')
vogal = 'aeiou'
for letra in range (0,len(palavras)):
    objeto = palavras[letra]
    voga = ''
    for i in objeto:
        if i in vogal:
            voga += i + ' '
    print(f'Na palavra {objeto.upper()} temos as vogais: {voga.upper()}' )



