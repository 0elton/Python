


a = int(input('OPERAÇÕES COM DUAS VARIAVEIS NUMÉRICAS:\nDigite o  valor de A: '))
b = int(input('Digite o  valor de B: '))

soma = a + b
subtracao = a - b
divisao = a / b
multiplicacao = a * b
resto = a % b
media = (a + b) / 2



print(f'''###USANDO F-STRING###\nO valor da soma é: {soma}\nO valor da subtracao é: {subtracao}\nO valor da multiplicação é: {multiplicacao} ''')
print('\n###USANDO String format###\nO valor da divisão é: {} com resto igual a {}'.format(divisao, resto))
print('A média é: ' + str(media))

#NÃO SERÁ EXECUTADO SE O MODULO FOR IMPORTADO
if __name__ ==  "__main__":
    print(type(resto))