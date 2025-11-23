"""nome = str(input('Digite o nome:'))
sp = nome.strip() # removi qualquer espaço que colocarem, tanto  no começo quanto no final
cap = sp.capitalize() # transforma sempre a primeira letra em maiuscula
santo = cap.split() # primeiro coloquei cada palavra em bloco.
pri = (santo[0]) # aqui indentifiquei qual bloco que eu quero.
sa = 'Santo' in pri # E aqui coloquei para busca uma palavra ispecifica. IN serve para indentificar uma palavra ispecifica e mostra se é verdadeiro ou falso.
print(sa) # aqui mandei mostrar o resultado."""

cid = str(input('Digite o nome de uma cidade: ')).strip() # O strip posso colocar direto no imput
print(cid[:5].upper() == 'SANTO' )
