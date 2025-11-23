nome = str(input('Digite seo nome: ')).strip()
g = nome.upper()
p = nome.lower()
se = nome.replace(" ","")# sempre lembrar que temos que colocar oque aeta dendo antes e o que queremos depois.
con = len(se)
pri = len(nome.split()[0])
print("""O seu nome em MAIUSCULA fica assim: {}.
O seu nome em minuscula fica assim: {}. 
O seu nome sem espaço fica assim: {}.
Seu nome contem {} caracteries sem contar espaços.
E seu primeiro nome tem {} caracteries.""". format(g,p, se, con,pri ))


nome2 = str(input('Digite seu nome: ')).strip()
print('Analizando seu nome...')
print("""Seu nome em Maiuscula fica assim {}.
Seu nome em minuscula fica assim {}.
Seu nome contem {} caracteries sem contar espaço.
Seu primeiro nome tem {} caracteries.""".format(nome2.upper(), nome2.lower(),len(nome2)- nome2.count(' '), len(nome.split()[0])))