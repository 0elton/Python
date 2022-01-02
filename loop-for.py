a = int(input("Verificar se o numero é primo: "))

div = 0
for x in range(1, a+1):
    resto = a % x
    if resto == 0:
        div += 1

if div == 2:
    print('Numero {} é primo'.format(a))
else:
    print('Numero {} não é primo'.format(a))



