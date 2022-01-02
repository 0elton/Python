a = int(input('Nota do primeiro bimestre: '))
while a > 10:
    a = int(input('Nota do primeiro bimestre: '))

b = int(input('Nota do segundo bimestre: '))
while b > 10:
    b = int(input('Nota do segundo bimestre: '))

c = int(input('Nota do terceiro bimestre: '))
while c > 10:
    c = int(input('Nota do terceiro bimestre: '))

d = int(input('Nota do quarto bimestre: '))
while d > 10:
    d = int(input('Nota do quarto bimestre: '))

media = (a + b + c + d) / 4

print('Media = {}'.format(media))