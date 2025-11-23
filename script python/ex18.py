impor
from math import sin, cos, tan, radians
an = float(input('Digite um Angulo que você deseja: '))
seno = sin(radians(an))
print('O seno do angulo de {} tem o SENO de {:.2f}'.format(an, seno))
cosseno = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
tangent = tan(radians(an))
print('O angulo de {} tem a angente de {:.2f}'.format(an, tangent))