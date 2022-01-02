
n = int(input("Verificar numeros primos até: "))

for a in range(1, n + 1):
    div = 0
    for x in range(1, a+1):
        resto = a % x
        if resto == 0:
            div += 1

    if div == 2:
        print('Numero {} é primo'.format(a))
    else:
        print('Numero {} não é primo'.format(a))