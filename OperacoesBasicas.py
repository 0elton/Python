


a = 10
b = 5

soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
resto = a % b

print(f'''###USANDO F-STRING###\nO valor da soma é: {soma}\nO valor da subtracao é: {subtracao}\nO valor da multiplicação é: {multiplicacao} ''')
print('\n###USANDO String format###\nO valor da divisão é: {} com resto igual a {}'.format(divisao, resto))


#NÃO SERÁ EXECUTADO SE O MODULO FOR IMPORTADO
if __name__ ==  "__main__":
    print(type(resto))
