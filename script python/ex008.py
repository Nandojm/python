metro = float(input('Digite os metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cent = metro * 100
mili = metro * 1000
print('A medida de {}m corresponde a: \n{}km \n{}hm '
      '\n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(metro, km, hm, dam, dm,cent, mili))