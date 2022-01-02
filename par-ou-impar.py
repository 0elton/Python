a = int(input('Entre com o um valor: '))

resto = a % 2

if resto == 0:
    print(f'''O número {a} é par''')
else:
    print(f'''O número {a} é impar''')