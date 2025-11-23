soma = 0
cont = 0
for c in range (1,7):
    nu = int(input('Digite o {} valor: '.format(c)))
    if nu % 2 == 1:# pegei o numero que vai ser digitado, dividi por 2 e se o resultado for igual 1, ele é um numero IMPÁ
        soma = soma + nu # aqui a soma que antes era 0 vai receber o primeiro numero e passa a ser ela + o proximo exp: SOMA = 0 recebe 1 e passa a ser 1, agora soma que agora é 1 recebe o proximo numero que é 3 e fica. SOMA que é 1 + NU que é 3 = 4 e assim sucecivaamente
        cont = cont + 1 # vai receber a quantidade de vezes que foi feita a verificação.
print('A verificação dos {} numeros soma um  total de {} '.format(cont,soma))