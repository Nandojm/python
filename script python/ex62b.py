primeiro = int(input('Primeiro termo: ')) # recebi a primeira informação
razao = int(input('Razão da PA: ')) # recebi a segunda informação
termo = primeiro # o termo ja assumiu o primeiro valor
cont = 1 # contador começou em um
total = 0 # totao começando com zero
mais = 10 # mais ja comeca com os 10 primeiro termos
while mais != 0: # este while dis que se so o numero digitado for diferente de zero, vai começar um repetição
    total = total + mais # total vai receber mais o (mais) que é igual a 10
    while cont <= total: # este while vai ser executado os 10 termos que está no 'mais'
        print(f'{termo} -> ', end='') # este print vai mostrar os 10 primeiros termos
        termo += razao # vai se somado o termo mais a razão
        cont += 1 # vai contar aquantas razoes foram feitas
    print('PAUSA')
    mais = int(input('Quantos termos vo^ce quer mostrar a mais? ')) # vai gerar um input para perguntar se vai querer continuar ou finalizar
print(f'Progressão finalizada com {total} mostrados')