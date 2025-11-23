mas = 'M'
fem = 'F'
sexo = 1

while sexo != mas and sexo != fem: # Aqui mandei ver se o usuario era masculino ou feminino. Se ele digitar uma resposta invalida, vai fazer a repetição.
    print('---'*10)
    sexo = str(input('Qual é o seu sexo ? [M/F] ')).upper()
    if sexo != mas and sexo != fem: # este if vai dizer que ele digitou uma resposta errada.
        print('Você digitou um sexo\033[31m INVALIDO\033[m!')
    elif sexo == mas: # Este elif vai aparecer se for masculino
        print('Você é do sexo MASCULINO!')
    elif sexo == fem: # Este elif vai aparecer se for mulher
        print('Você é do sexo FEMININO!')

