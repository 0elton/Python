


a = 15
b = 7

soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
resto = a % b
exponenciacao = a ** b
parte_inteira = a // b

print(f'''###USANDO F-STRING###\nO valor da soma é: {soma}\nO valor da subtracao é: {subtracao}\nO valor da multiplicação é: {multiplicacao} ''')
print('\n###USANDO String format###\nO valor da divisão é: {} com resto igual a {}'.format(divisao, resto))
print('\nValor de {} elevado a {} é: {}'.format(a, b,exponenciacao))
print('\nParte inteira da divisão é: {}'.format(parte_inteira))

#NÃO SERÁ EXECUTADO SE O MODULO FOR IMPORTADO
if __name__ ==  "__main__":
    print(type(resto))
