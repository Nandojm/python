lista = []
css = ('-' * 15)
numero = None
while True:
    print(css)
    nome = str(input('Nome: '))
    try:
        numero = int(input('Número do funcionario: '))
    except ValueError:
        print('Apenas numeros')
    lista.append(nome)
    lista.append(numero)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]?')).upper()
    if continuar in 'N':
        break
print(css)
for i in range(0,len(lista),2):
    nom = lista[i]
    nu = lista[i + 1]
    print(f"""Nome: {nom} 
Número: {nu}""")
    print(css)