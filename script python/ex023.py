nu = int(input('Digite um numero de 0 a 9999: '))
un = nu // 1 % 10
dz = nu // 10 % 10
ce = nu // 100 % 10
mi = nu // 1000 % 10
print("""
Unidade:{}
Dezena:{}
Centana:{}
Milhar:{}""".format(un, dz,ce,mi))
