dia = float(input('Digite os numeros de dia: '))

horas = dia * 24
minutos = horas * 60
segundos = minutos * 60
print("""
{:.0f} dia(s) tem
{:.0f} hora(s)
{:.0f} minuto(s)
{:.0f} segundo(s)""".format(dia, horas, minutos, segundos))

